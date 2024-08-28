# test_api.py
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["title"] == "foo"
    assert json_response["body"] == "bar"
    assert json_response["userId"] == 1

def test_update_post():
    post_id = 1
    payload = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["title"] == "updated title"
    assert json_response["body"] == "updated body"

def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
