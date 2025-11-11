from api.route import SampleScrapingAPI
from utils.log import get_logger

logger = get_logger(__name__)


def main():
    SampleScrapingAPI().extract_data()


if __name__ == "__main__":
    main()
