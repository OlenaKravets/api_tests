import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    payload = {
        "title": "My automated post",
        "body": "This post was created via API test",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == payload["title"]
