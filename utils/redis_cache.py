from datetime import datetime, timezone
from functools import cache

from constants import REDIS_URI
from redis import Redis


@cache
def get_redis_connection():
    """
    Get a connection to the Redis cache.

    This function returns a Redis connection object, which can be used
    to interact with the Redis cache. The connection is cached, so
    subsequent calls to this function will return the same connection
    object.

    Returns:
        Redis: A Redis connection object.
    """
    if REDIS_URI is None:
        raise NotImplementedError("Value for env: REDIS_URI is not set.")
    return Redis.from_url(REDIS_URI)


def save_key_to_cache(key: str):
    """
    Save a key to the Redis cache.

    This function saves a key to the Redis cache, associating it with the current
    time in UTC. The key can later be retrieved using the `key_exists_in_cache`
    function.

    Args:
        key (str): The key to be saved to the Redis cache.

    Returns:
        None
    """
    get_redis_connection().set(key, str(datetime.now(timezone.utc)))


def key_exists_in_cache(key) -> bool:
    """
    Check if a key exists in the Redis cache.

    Args:
        key (str): The key to check for in the Redis cache.

    Returns:
        bool: True if the key exists in the Redis cache, False otherwise.

    """
    return get_redis_connection().exists(key) == 1


def test_redis_connection() -> bool:
    """
    Test the Redis connection by sending a PING command.

    This function attempts to ping the Redis server to check if the connection
    is active and responsive.

    Returns:
        bool: True if the Redis server responds to the PING command, False otherwise.
    """
    return get_redis_connection().ping()
