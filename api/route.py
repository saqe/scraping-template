import tenacity

from constants import DEBUG
from utils.http_requests import RequestAPI
from utils.log import get_logger
from utils.exceptions import TooManyRequests

logger = get_logger(__name__)


class SampleScrapingAPI(RequestAPI):
    MAIN_URL = "https://api.ipify.org"

    def extract_data(self):
        response = self.session.get(self.MAIN_URL, params={"format": "json"})

        response.raise_for_status()

        logger.info(response.json())

    @tenacity.retry(
        wait=tenacity.wait_fixed(30),
        retry=tenacity.retry_if_exception_type(TooManyRequests),
        stop=tenacity.stop_after_attempt(3),
    )
    def multiple_hit_until_found(self):
        response = self.session.get(self.MAIN_URL, params={"format": "json"})

        if response.status_code == 429:
            logger.warning("Rate Limiting by API.")
            raise TooManyRequests(
                "You are sending too many requests to the server, hold on man"
            )
        return response

    @staticmethod
    def dangerous_route():
        if DEBUG:
            logger.warning("Skipping with DEBUG flag on.")
        else:
            logger.info("Executed, DEBUG OFF")
