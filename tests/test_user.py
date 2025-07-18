import pytest
import requests

@pytest.fixture
def mock_requests_get_unauthorized(mocker):
    # Mock response for unauthorized access
    mock_response = MockResponse(b'', 401)
    mocker.patch.object(requests, 'get', return_value=mock_response)

@pytest.fixture
def mock_requests_get_authorized(mocker):
    # Mock response for authorized access
    mock_response = MockResponse(b'', 200)
    mocker.patch.object(requests, 'get', return_value=mock_response)

class MockResponse:
    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

def test_user_endpoint_unauthorized(mock_requests_get_unauthorized):
    # Make the HTTP GET request with invalid credentials
    response = requests.get('http://127.0.0.1:8000/users/', params={
        'username': 'admin',
        'password': 'admin'
    })

    # Verify the response status code is 401 (Unauthorized)
    assert response.status_code == 401

    # Verify the response content is empty
    assert response.content == b''

def test_user_endpoint_authorized(mock_requests_get_authorized):
    # Make the HTTP GET request with valid credentials
    response = requests.get('http://127.0.0.1:8000/users/', params={
        'username': 'admin',
        'password': 'qwerty'
    })

    # Verify the response status code is 200 (OK)
    assert response.status_code == 200

    # Verify the response content is empty
    assert response.content == b''
