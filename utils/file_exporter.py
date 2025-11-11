import os

import boto3

from constants import S3_BUCKET_NAME
from utils.log import get_logger

logger = get_logger(__name__)


class BlobFileExporter:
    """
        ENVs must required are
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY
        - AWS_ENDPOINT_URL_S3
        - S3_BUCKET_NAME (Can be set at constants.py)
    """

    def __init__(self):
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws_endpoint_url_s3 = os.getenv("AWS_ENDPOINT_URL_S3")
        self.s3_bucket_name = S3_BUCKET_NAME  # Default from constants, can be overridden by env var if needed

        self._validate_envs()
        self.s3_client = self._get_s3_client()

    def _validate_envs(self):
        if not self.aws_access_key_id or not self.aws_secret_access_key:
            raise EnvironmentError("AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY must be set in environment variables.")
        if not self.aws_endpoint_url_s3:
            raise EnvironmentError("AWS_ENDPOINT_URL_S3 must be set in environment variables for AWS alernatives.")
        if not self.s3_bucket_name:
            raise EnvironmentError("S3_BUCKET_NAME must be set in constants.py or as an environment variable.")

    def _get_s3_client(self):
        session = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )
        if self.aws_endpoint_url_s3:
            return session.client("s3", endpoint_url=self.aws_endpoint_url_s3)
        return session.client("s3")

    def upload_file(self, file_path: str, object_name: str = None) -> dict:
        """
        Uploads a file to an S3 bucket.

        :param file_path: Path to the file to upload.
        :param object_name: S3 object name. If not specified then file_path is used.
        :return: Dictionary containing the response from S3 if successful, otherwise raises an exception.
        """
        if object_name is None:
            object_name = os.path.basename(file_path)

        try:
            with open(file_path, "rb") as f:
                response = self.s3_client.put_object(
                    Bucket=self.s3_bucket_name,
                    Key=object_name,
                    Body=f
                )
            logger.info(f"File {file_path} uploaded to {self.s3_bucket_name}/{object_name}")
            return response
        except FileNotFoundError:
            logger.error(f"The file {file_path} was not found.")
            raise
        except Exception as e:
            logger.error(f"Error uploading file {file_path} to S3: {e}")
            raise
