import pytest
from unittest.mock import MagicMock, patch
import requests
import tenacity

from api.route import SampleScrapingAPI
from utils.exceptions import TooManyRequests
from constants import DEBUG


@pytest.fixture
def mock_session_get():
    """Fixture to mock requests.Session.get."""
    with patch("requests.Session.get") as mock_get:
        yield mock_get


def test_extract_data_success(mock_session_get):
    """Test extract_data method for successful response."""
    # Mock a successful response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"ip": "127.0.0.1"}
    mock_session_get.return_value = mock_response

    # Call the method
    api = SampleScrapingAPI()
    api.extract_data()

    # Assertions
    mock_session_get.assert_called_once_with(api.MAIN_URL, params={"format": "json"})
    mock_response.raise_for_status.assert_called_once()
    assert mock_response.json.called


def test_extract_data_http_error(mock_session_get):
    """Test extract_data method for HTTP error."""
    # Mock an HTTP error response
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Not Found")
    mock_session_get.return_value = mock_response

    # Call the method and expect an exception
    api = SampleScrapingAPI()
    with pytest.raises(requests.exceptions.HTTPError):
        api.extract_data()

    # Assertions
    mock_session_get.assert_called_once_with(api.MAIN_URL, params={"format": "json"})
    mock_response.raise_for_status.assert_called_once()


def test_multiple_hit_until_found_success(mock_session_get):
    """Test multiple_hit_until_found method for successful response after retries."""
    # Mock responses: first two are 429, third is 200
    mock_response_429 = MagicMock()
    mock_response_429.status_code = 429

    mock_response_200 = MagicMock()
    mock_response_200.status_code = 200
    mock_response_200.json.return_value = {"status": "ok"} # Add a return value for json()

    mock_session_get.side_effect = [mock_response_429, mock_response_429, mock_response_200]

    api = SampleScrapingAPI()
    response = api.multiple_hit_until_found()

    assert mock_session_get.call_count == 3
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_multiple_hit_until_found_failure(mock_session_get):
    """Test multiple_hit_until_found method for failure after all retries."""
    # Mock responses: all three are 429
    mock_response_429 = MagicMock()
    mock_response_429.status_code = 429
    mock_session_get.side_effect = [mock_response_429, mock_response_429, mock_response_429]

    api = SampleScrapingAPI()
    with pytest.raises(tenacity.RetryError):
        api.multiple_hit_until_found()

    assert mock_session_get.call_count == 3


def test_dangerous_route_debug_on(mocker):
    """Test dangerous_route when DEBUG is True."""
    mocker.patch("api.route.DEBUG", True)
    mock_logger_warning = mocker.patch("api.route.logger.warning")

    SampleScrapingAPI.dangerous_route()

    mock_logger_warning.assert_called_once_with("Skipping with DEBUG flag on.")


def test_dangerous_route_debug_off(mocker):
    """Test dangerous_route when DEBUG is False."""
    mocker.patch("api.route.DEBUG", False)
    mock_logger_info = mocker.patch("api.route.logger.info")

    SampleScrapingAPI.dangerous_route()

    mock_logger_info.assert_called_once_with("Executed, DEBUG OFF")
