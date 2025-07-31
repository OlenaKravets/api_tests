import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
