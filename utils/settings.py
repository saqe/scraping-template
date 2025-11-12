from constants import DEBUG, REDIS_URI
from utils.log import get_logger
from utils.redis_cache import test_redis_connection

logger = get_logger(__name__)

if not DEBUG and REDIS_URI:
    logger.info("Testing redis connection")
    test_redis_connection()
