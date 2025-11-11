import pytest
from fakeredis import FakeStrictRedis

from utils.redis_cache import get_redis_connection, key_exists_in_cache, save_key_to_cache


@pytest.fixture(autouse=True)
def mock_redis(mocker):
    """Mock the Redis connection for all tests."""
    mock_redis_conn = FakeStrictRedis()
    mocker.patch("utils.redis_cache.get_redis_connection", return_value=mock_redis_conn)
    return mock_redis_conn


def test_key_exists_in_cache():
    """Test that key_exists_in_cache returns True for an existing key."""
    # Given
    key = "test_key"
    save_key_to_cache(key)

    # When
    exists = key_exists_in_cache(key)

    # Then
    assert exists is True


def test_key_does_not_exist_in_cache():
    """Test that key_exists_in_cache returns False for a non-existing key."""
    # Given
    key = "non_existing_key"

    # When
    exists = key_exists_in_cache(key)

    # Then
    assert exists is False


def test_save_key_to_cache(mock_redis):
    """Test that save_key_to_cache correctly saves a key to the cache."""
    # Given
    key = "new_test_key"

    # When
    save_key_to_cache(key)

    # Then
    assert mock_redis.exists(key) == 1
