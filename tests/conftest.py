import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def inventory_url():
    return "https://www.saucedemo.com/inventory.html"

@pytest.fixture(scope="session")
def api_base_url():
    return "https://jsonplaceholder.typicode.com"