import pytest
from unittest.mock import MagicMock, patch
import requests

from utils.http_requests import RequestAPI
from constants import REQUEST_HEADERS, HTTP_PROXY


class ConcreteRequestAPI(RequestAPI):
    MAIN_URL = "http://test.com"


@patch("requests.Session")
def test_request_api_init_no_proxy(mock_session_class, mocker):
    """Test RequestAPI __init__ when HTTP_PROXY is not set."""
    mocker.patch("utils.http_requests.HTTP_PROXY", None) # Patch directly
    mock_instance = mock_session_class.return_value

    api = ConcreteRequestAPI()

    mock_session_class.assert_called_once()
    mock_instance.headers.update.assert_called_once_with(REQUEST_HEADERS)
    mock_instance.proxies.update.assert_not_called() # Check that proxy is not enabled
    assert api.session == mock_instance


@patch("requests.Session")
def test_request_api_init_with_proxy(mock_session_class, mocker):
    """Test RequestAPI __init__ when HTTP_PROXY is set."""
    mocker.patch("utils.http_requests.HTTP_PROXY", "http://myproxy.com") # Patch directly
    mock_instance = mock_session_class.return_value

    api = ConcreteRequestAPI()

    mock_session_class.assert_called_once()
    mock_instance.headers.update.assert_called_once_with(REQUEST_HEADERS)
    mock_instance.proxies.update.assert_called_once_with({"http": "http://myproxy.com", "https": "http://myproxy.com"}) # Use the patched value
    assert api.session == mock_instance


def test_enable_proxy(mocker):
    """Test enable_proxy method."""
    mocker.patch("utils.http_requests.HTTP_PROXY", "http://myproxy.com") # Patch directly
    api = ConcreteRequestAPI()
    api.session = MagicMock() # Mock the session object

    api.enable_proxy()

    api.session.proxies.update.assert_called_once_with({"http": "http://myproxy.com", "https": "http://myproxy.com"}) # Use the patched value
