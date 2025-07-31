import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Post updated successfully",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["title"] == "Updated Title"
