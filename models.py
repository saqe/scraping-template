from functools import cached_property
from typing import Optional, Dict, List, Literal, Union

from pydantic import (
    BaseModel,
    PositiveInt,
    HttpUrl,
    field_validator,
    model_validator,
    computed_field,
    Field,
    AliasPath,
    NonNegativeInt,
    UUID1,
    UUID4,
)

from constants import CONSTANT_ID


class SampleModel(BaseModel):
    id: Union[UUID1, UUID4]
    positive_id: PositiveInt = Field(alias="positiveID")
    price: NonNegativeInt = Field(alias="price")

    name: str = Field(alias="display_name")

    option_link: Optional[HttpUrl] = Field(alias="desktop_href")

    colors: List[str]
    records: List[Dict]

    this_or_that: Union[int, float, None]

    options_type: Literal["option_one", "option_two"] = Field(
        validation_alias=AliasPath("grand_parent", "child"), default=None
    )

    @computed_field
    @cached_property
    def is_constant_matched(self) -> bool:
        return self.positive_id == CONSTANT_ID

    @computed_field
    def selector(self) -> tuple | None:
        query_selector = self.option_link.query_params()
        if query_selector:
            return tuple(query_selector[0])
        return None

    @field_validator("positive_id", mode="before")
    @classmethod
    def validate_seller_id(cls, v: str) -> Optional[PositiveInt]:
        """Clear out M from the Positive id and convert the value to int"""
        return v and int(v.lstrip("M")) or None

    @model_validator(mode="after")
    def name_must_contain_space(self):
        if self.positive_id == 1 and self.price == 0:
            raise ValueError("Error Message goes here.")

        return self
