from os import getenv

CONSTANT_ID = ""

REDIS_URI = getenv("REDIS_URI")

CHROME_BROWSER_PATH = getenv("CHROME_BROWSER_PATH", "/opt/chrome/chrome")
CHROME_DRIVER_PATH = getenv("CHROME_DRIVER_PATH", "/opt/chromedriver")
