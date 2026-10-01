import pytest
import requests
from api.api_client import ApiClient

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(api_base_url, user_id):
    client = ApiClient()

    response = client.get(f"{api_base_url}/users/{user_id}")

    assert response.status_code == requests.codes.ok
    assert response.json()["id"] == user_id

def test_get_user_data(api_base_url):
    client = ApiClient()

    response = client.get(f"{api_base_url}/users/1")
    user = response.json()

    assert response.status_code == requests.codes.ok
    assert user["name"] == "Leanne Graham"
    assert user["username"] == "Bret"
    assert user["email"] == "Sincere@april.biz"

@pytest.mark.regression
def test_create_user(api_base_url):
    client = ApiClient()

    data = {
        "name": "Tomislav Drljaca",
        "username": "tomislav",
        "email": "tomislav@example.com"
    }

    response = client.post(
        f"{api_base_url}/users",
        data
    )

    assert response.status_code == requests.codes.created
    assert response.json()["name"] == "Tomislav Drljaca"

def test_get_non_existing_user(api_base_url):
    client = ApiClient()

    response = client.get(f"{api_base_url}/users/9999")

    assert response.status_code == requests.codes.not_found