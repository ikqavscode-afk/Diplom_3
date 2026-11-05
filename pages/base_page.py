from collections.abc import Callable

import allure

import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import settings
from locators import header_locators

Locator = tuple[str, str]
DRAG_AND_DROP_JS = """
const dataTransfer = new DataTransfer();
const fire = (element, type) => element.dispatchEvent(
    new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer})
);
const [source, target] = arguments;
fire(source, 'dragstart');
fire(target, 'dragenter');
fire(target, 'dragover');
fire(target, 'drop');
fire(source, 'dragend');
"""


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.timeout)

    @allure.step("Открыть страницу {path}")
    def open(self, path: str = "/") -> None:
        self.driver.get(f"{settings.base_url}{path}")

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator: Locator) -> None:
        def click_element(driver: WebDriver) -> bool:
            element = EC.element_to_be_clickable(locator)(driver)
            if not element:
                return False
            element.click()
            return True

        WebDriverWait(
            self.driver,
            settings.timeout,
            ignored_exceptions=(
                NoSuchElementException,
                ElementClickInterceptedException,
            ),
        ).until(click_element)

    def type_text(self, locator: Locator, text: str) -> None:
        with allure.step(f"Ввести текст в поле {locator}"):
            field = self.find(locator)
            field.clear()
            field.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.find(locator)
        except TimeoutException:
            return False
        return True

    def find_present(self, locator: Locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_all(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)
    
    def wait_until(self, condition: Callable[[], bool]) -> None:
        self.wait.until(lambda _: condition())

    def wait_invisible(self, locator: Locator) -> bool:
        return bool(self.wait.until(EC.invisibility_of_element_located(locator)))

    @allure.step("Перетащить {source} в {target}")
    def drag_and_drop(self, source: Locator, target: Locator) -> None:
        self.driver.execute_script(
            DRAG_AND_DROP_JS, self.find(source), self.find(target)
        )

    @allure.step("Перейти в «Конструктор»")
    def go_to_constructor(self) -> None:
        self.click(header_locators.CONSTRUCTOR_LINK)

    @allure.step("Перейти в «Ленту заказов»")
    def go_to_order_feed(self) -> None:
        self.click(header_locators.ORDER_FEED_LINK)
