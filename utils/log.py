import logging
from datetime import datetime
from os import makedirs

# Create logs directory if not exists
makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(funcName)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(datetime.now().strftime("logs/log_%Y-%m-%d.log")),
        logging.StreamHandler(),  # also print logs to console
    ],
)


def get_logger(name):
    return logging.getLogger(name)
