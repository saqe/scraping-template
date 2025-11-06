from requests import RequestException

class ProductNotFound(Exception):
    pass


class TooManyRequests(RequestException):
    """Too many requests"""
