import os
import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"
HEADERS = {
    "x-api-key": os.getenv("REQRES_API_KEY", "reqres-free-v1"),  # API KEY з GitHub Secrets або локально
    "Content-Type": "application/json"
}

@allure.feature("Users API")
class TestUsersAPI:

    @allure.story("Get list of users")
    def test_get_users_list(self):
        """Перевірка отримання списку користувачів"""
        with allure.step("Відправляю GET-запит"):
            response = requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)
            allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        with allure.step("Перевіряю статус код 200"):
            assert response.status_code == 200

        with allure.step("Перевіряю, що список користувачів не порожній"):
            data = response.json()
            assert "data" in data
            assert len(data["data"]) > 0

    @allure.story("Get single user - позитивні кейси")
    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_single_user_positive(self, user_id):
        """Перевірка отримання даних існуючого користувача"""
        with allure.step(f"Відправляю GET-запит для користувача {user_id}"):
            response = requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
            allure.attach(response.text, f"User {user_id} Response", allure.attachment_type.JSON)

        with allure.step("Перевіряю код відповіді 200"):
            assert response.status_code == 200

        with allure.step("Перевіряю правильний ID"):
            assert response.json()["data"]["id"] == user_id

    @allure.story("Get single user - неіснуючий користувач")
    def test_get_single_user_not_found(self):
        """Перевірка отримання неіснуючого користувача (очікуваний 404)"""
        with allure.step("Відправляю GET-запит для користувача з ID 9999"):
            response = requests.get(f"{BASE_URL}/users/9999", headers=HEADERS)
            allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        with allure.step("Перевіряю код 404"):
            assert response.status_code == 404

    @allure.story("Create new user")
    def test_create_user(self):
        """Створення нового користувача"""
        payload = {
            "name": "TestUser",
            "job": "QA Engineer"
        }
        with allure.step("Відправляю POST-запит"):
            response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
            allure.attach(response.text, "Create User Response", allure.attachment_type.JSON)

        with allure.step("Перевіряю статус код 201"):
            assert response.status_code == 201

        with allure.step("Перевіряю ім'я користувача"):
            assert response.json()["name"] == "TestUser"

    @allure.story("Create user - відсутні дані")
    def test_create_user_missing_fields(self):
        """Спроба створити користувача без обов'язкових полів (очікуваний 400 або 422)"""
        payload = {}
        with allure.step("Відправляю POST-запит з порожнім payload"):
            response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
            allure.attach(response.text, "Invalid Create User Response", allure.attachment_type.JSON)

        with allure.step("Перевіряю статус код (не має бути 201)"):
            assert response.status_code in [400, 422]

    @allure.story("Update user")
    def test_update_user(self):
        """Оновлення даних користувача"""
        payload = {
            "name": "UpdatedUser",
            "job": "Automation QA"
        }
        with allure.step("Відправляю PUT-запит"):
            response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)
            allure.attach(response.text, "Update User Response", allure.attachment_type.JSON)

        with allure.step("Перевіряю код відповіді 200"):
            assert response.status_code == 200

        with allure.step("Перевіряю, що job оновлено"):
            assert response.json()["job"] == "Automation QA"

    @allure.story("Delete user")
    def test_delete_user(self):
        """Видалення користувача"""
        with allure.step("Відправляю DELETE-запит"):
            response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
            allure.attach(response.text, "Delete User Response", allure.attachment_type.TEXT)

        with allure.step("Перевіряю код відповіді 204"):
            assert response.status_code == 204

    @allure.story("Access without API key")
    def test_access_without_api_key(self):
        """Перевірка доступу без API ключа (очікуваний 401)"""
        with allure.step("Відправляю GET-запит без API KEY"):
            response = requests.get(f"{BASE_URL}/users?page=2")
            allure.attach(response.text, "Response without token", allure.attachment_type.JSON)

        with allure.step("Перевіряю, що доступ заборонено"):
            assert response.status_code == 401
