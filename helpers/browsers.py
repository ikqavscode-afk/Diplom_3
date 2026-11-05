from collections.abc import Callable

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


def _chrome(headless: bool) -> WebDriver:
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    if headless:
        options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)


def _firefox(headless: bool) -> WebDriver:
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    if headless:
        options.add_argument("-headless")
    return webdriver.Firefox(options=options)


BROWSERS: dict[str, Callable[[bool], WebDriver]] = {
    "chrome": _chrome,
    "firefox": _firefox,
}


def create_driver(name: str, headless: bool = False) -> WebDriver:
    return BROWSERS[name](headless)
