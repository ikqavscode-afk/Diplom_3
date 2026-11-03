import allure

from data import endpoints
from locators import order_feed_locators as locators
from pages.base_page import BasePage, Locator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

class OrderFeedPage(BasePage):
    @allure.step("Открыть ленту заказов")
    def open_order_feed(self) -> None:
        self.open(endpoints.ORDER_FEED_PAGE)

    def is_title_visible(self) -> bool:
        return self.is_visible(locators.FEED_TITLE)

    def get_total_completed(self) -> int:
        return int(self.get_text(locators.TOTAL_COMPLETED_COUNT))

    def get_today_completed(self) -> int:
        return int(self.get_text(locators.TODAY_COMPLETED_COUNT))

    @allure.step("Дождаться, пока «Выполнено за все время» станет больше {value}")
    def wait_total_completed_above(self, value: int) -> bool:
        return self._wait_counter_above(locators.TOTAL_COMPLETED_COUNT, value)

    @allure.step("Дождаться, пока «Выполнено за сегодня» станет больше {value}")
    def wait_today_completed_above(self, value: int) -> bool:
        return self._wait_counter_above(locators.TODAY_COMPLETED_COUNT, value)

    def _wait_counter_above(self, locator: Locator, value: int) -> bool:
        try:
            self.wait.until(
                lambda driver: (text := driver.find_element(*locator).text).isdigit() and int(text) > value
            )
        except TimeoutException:
            return False
        return True

    @allure.step("Проверить, что заказ {number} есть в разделе «В работе»")
    def is_order_in_progress(self, number: int) -> bool:
        try:
            self.wait.until(lambda driver: number in self._in_progress_numbers(driver))
        except TimeoutException:
            return False
        return True

    @staticmethod
    def _in_progress_numbers(driver: WebDriver) -> list[int]:
        items = driver.find_elements(*locators.ORDERS_IN_PROGRESS)
        return [int(item.text) for item in items if item.text.isdigit()]
    