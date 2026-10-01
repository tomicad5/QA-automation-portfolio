import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_valid_login(page: Page, base_url, inventory_url):
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert page.url == inventory_url

@pytest.mark.regression
def test_invalid_login(page: Page, base_url):
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in login_page.get_error_message()

@pytest.mark.regression
def test_locked_out_user(page: Page, base_url):
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.error_message.is_visible()
    assert "Sorry, this user has been locked out" in login_page.get_error_message()

@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ],
)
def test_valid_users(page: Page, base_url, inventory_url, username, password):
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login(username, password)

    assert page.url == inventory_url