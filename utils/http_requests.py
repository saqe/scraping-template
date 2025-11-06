import requests
from constants import REQUEST_HEADERS, HTTP_PROXY


class RequestAPI:
    MAIN_URL = ""

    def enable_proxy(self):
        self.session.proxies.update({"http": HTTP_PROXY, "https": HTTP_PROXY})

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(REQUEST_HEADERS)
