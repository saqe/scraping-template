import requests
from requests import RequestException

class ProductNotFound(Exception):
    pass


class TooManyRequests(RequestException):
    """Too many requests"""

class ServerError(RequestException):
    """Server Internal Error"""

def is_403_rate_limiting(exception: Exception) -> bool:
    """
    Predicate for `tenacity` to catch 403 HTTP errors (rate limiting).

    Args:
        exception: The exception to check.

    Returns:
        True if the exception is an HTTP 403 error, False otherwise.
    """
    return (isinstance(exception, requests.exceptions.HTTPError) and
            exception.response.status_code == 403)

def is_500_server_internal_error(exception: Exception) -> bool:
    """
    Predicate for `tenacity` to catch 500 HTTP errors (server internal error).

    Args:
        exception: The exception to check.

    Returns:
        True if the exception is an HTTP 500 error, False otherwise.
    """
    return (isinstance(exception, requests.exceptions.HTTPError) and
            exception.response.status_code == 500)
