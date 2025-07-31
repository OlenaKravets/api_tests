import pytest
import allure
from utils.api_client import APIClient

@allure.feature("Posts API")
class TestPostsCRUD:

    @pytest.fixture(scope="class")
    def client(self, base_url):
        return APIClient(base_url)

    @allure.story("Create Post")
    def test_create_post(self, client, headers):
        payload = {
            "title": "My automated post",
            "body": "Post created via extended test",
            "userId": 1
        }
        response = client.post("/posts", json=payload, headers=headers)
        assert response.status_code == 201
        json_data = response.json()
        allure.attach(str(json_data), name="Response Body", attachment_type=allure.attachment_type.TEXT)
        assert json_data["title"] == payload["title"]
        self.post_id = json_data["id"]

    @allure.story("Get Existing Post")
    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post(self, client, post_id):
        response = client.get(f"/posts/{post_id}")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["id"] == post_id

    @allure.story("Update Post")
    def test_update_post(self, client, headers):
        payload = {
            "id": 1,
            "title": "Updated Title Extended",
            "body": "Post updated successfully",
            "userId": 1
        }
        response = client.put("/posts/1", json=payload, headers=headers)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["title"] == "Updated Title Extended"

    @allure.story("Delete Post")
    def test_delete_post(self, client):
        response = client.delete("/posts/1")
        assert response.status_code == 200
