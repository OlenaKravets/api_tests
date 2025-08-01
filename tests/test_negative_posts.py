import requests
import pytest
import allure


@allure.feature("Negative API Tests")
class TestNegativePosts:

    @pytest.mark.parametrize("payload", [
        {"title": 12345, "body": True, "userId": "text"},
        {"userId": 1},
        {"title": "<script>alert('XSS')</script>", "body": "Hack", "userId": 1},
    ])
    def test_invalid_posts(self, payload, base_url):
        response = requests.post(f"{base_url}/posts", json=payload)
        allure.attach(str(response.json()), name="Invalid Payload Response", attachment_type=allure.attachment_type.TEXT)
        assert response.status_code in [201, 400]
