import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}
