import pytest
from utils.api_client import APIClient

BASE_URL = "https://api.example.com"

@pytest.fixture(scope="module")
def api_client():
    return APIClient(base_url=BASE_URL)

def test_get_endpoint(api_client):
    response = api_client.get("/endpoint")
    assert response.status_code == 200
    assert "expected_key" in response.json()

def test_post_endpoint(api_client):
    payload = {"key": "value"}
    response = api_client.post("/endpoint", json=payload)
    assert response.status_code == 201
    assert response.json()["key"] == "value"
