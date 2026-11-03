from collections.abc import Iterator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from api.user_client import UserClient
from data.models import User
from helpers.browsers import BROWSERS, create_driver
from helpers.generators import build_user
from pages.login_page import LoginPage

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--headless", action="store_true", help="Run browsers without a window")


@pytest.fixture
def user() -> Iterator[User]:
    client = UserClient()
    new_user = client.register(build_user())
    yield new_user
    client.delete(new_user)


@pytest.fixture(params=list(BROWSERS))
def driver(request: pytest.FixtureRequest) -> Iterator[WebDriver]:
    browser = create_driver(request.param, request.config.getoption("--headless"))
    yield browser
    browser.quit()

@pytest.fixture
def logged_in_driver(driver: WebDriver, user: User) -> WebDriver:
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user)
    return driver
