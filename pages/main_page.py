import allure

from data import endpoints
from locators import main_page_locators as locators
from pages.base_page import BasePage

ORDER_NUMBER_PLACEHOLDER = "9999"

class MainPage(BasePage):
   
    @allure.step("Открыть главную страницу")
    def open_main_page(self) -> None:
        self.open(endpoints.MAIN_PAGE)
   
    @allure.step("Кликнуть по ингредиенту")
    def click_bun_card(self) -> None:
        self.click(locators.BUN_CARD)

    def is_ingredient_modal_visible(self) -> bool:
        return self.is_visible(locators.INGREDIENT_MODAL_TITLE)
   
    @allure.step("Закрыть окно крестиком")
    def close_modal(self) -> None:
        self.click(locators.MODAL_CLOSE_BUTTON)

    def is_modal_closed(self) -> bool:
        return self.wait_invisible(locators.OPENED_MODAL)
    
    def get_bun_counter(self) -> int:
        return int(self.get_text(locators.BUN_COUNTER))

    @allure.step("Добавить булку в заказ")
    def add_bun_to_order(self) -> None:
        self.drag_and_drop(locators.BUN_CARD, locators.CONSTRUCTOR_BASKET)

    @allure.step("Оформить заказ")
    def make_order(self) -> int:
        self.click(locators.ORDER_BUTTON)
        self.wait.until(
            lambda driver: driver.find_element(*locators.ORDER_NUMBER).text
            not in ("", ORDER_NUMBER_PLACEHOLDER)
        )
        return int(self.get_text(locators.ORDER_NUMBER))

    def is_main_title_visible(self) -> bool:
        return self.is_visible(locators.MAIN_TITLE)