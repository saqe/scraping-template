from datetime import datetime
from enum import StrEnum
from os import getenv

CONSTANT_ID = ""


class SampleLocaleEnum(StrEnum):
    DE = "de-DE"  # Germany
    EN = "en-GB"  # English
    FR = "fr-FR"  # France
    ES = "es-ES"  # Spain
    IT = "it-IT"  # Italy
    PL = "pl-PL"  # Poland
    RO = "ro-RO"  # Romania


HTTP_PROXY = getenv("HTTP_PROXY")

DEBUG: bool = False

REQUEST_HEADERS = {
    "accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "content-type": "application/json",
}

REDIS_URI = getenv("REDIS_URI")

CHROME_BROWSER_PATH = getenv("CHROME_BROWSER_PATH", "/opt/chrome/chrome")
CHROME_DRIVER_PATH = getenv("CHROME_DRIVER_PATH", "/opt/chromedriver")


# Windows doesn't support having : in the file name.
CSV_FILE_NAME = str(str(datetime.today())[:16]).replace(":", "-") + ".csv"

# NOTE: Make sure header do not repeat.
CSV_FILE_HEADER = ["id", "name", "2", "3"]
CSV_FILE_HEADER.append("datetime")

# AWS S3 Bucket Name
S3_BUCKET_NAME = getenv('S3_BUCKET_NAME')
