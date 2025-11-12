from api.route import SampleScrapingAPI
from utils.log import get_logger
from utils.redis_cache import test_redis_connection

logger = get_logger(__name__)


# Test if redis connection is working
# test_redis_connection()


def main():
    SampleScrapingAPI().extract_data()


if __name__ == "__main__":
    main()
