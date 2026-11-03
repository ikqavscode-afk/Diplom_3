import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import settings

Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.timeout)

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Открыть страницу {path}")
    def open(self, path: str = "/") -> None:
        self.driver.get(f"{settings.base_url}{path}")

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.find(locator)
        except TimeoutException:
            return False
        return True

    def wait_invisible(self, locator: Locator) -> bool:
        return bool(self.wait.until(EC.invisibility_of_element_located(locator)))