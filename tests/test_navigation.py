import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Основная функциональность")
@allure.story("Навигация")
class TestNavigation:
    @allure.title("Клик по «Конструктор» открывает главную страницу")
    def test_constructor_link_opens_main_page(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()

        feed_page.go_to_constructor()

        assert MainPage(driver).is_main_title_visible()

    @allure.title("Клик по «Лента заказов» открывает ленту заказов")
    def test_order_feed_link_opens_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.go_to_order_feed()

        assert OrderFeedPage(driver).is_title_visible()
