import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title(
        "При создании нового заказа счётчик «Выполнено за все время» увеличивается"
    )
    def test_new_order_increases_total_completed(self, logged_in_driver):
        feed_page = OrderFeedPage(logged_in_driver)
        feed_page.go_to_order_feed()
        total_before = feed_page.get_total_completed()
        feed_page.go_to_constructor()

        MainPage(logged_in_driver).create_order()
        feed_page.go_to_order_feed()

        assert feed_page.wait_total_completed_above(total_before)

    @allure.title(
        "При создании нового заказа счётчик «Выполнено за сегодня» увеличивается"
    )
    def test_new_order_increases_today_completed(self, logged_in_driver):
        feed_page = OrderFeedPage(logged_in_driver)
        feed_page.go_to_order_feed()
        today_before = feed_page.get_today_completed()
        feed_page.go_to_constructor()

        MainPage(logged_in_driver).create_order()
        feed_page.go_to_order_feed()

        assert feed_page.wait_today_completed_above(today_before)

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_number_appears_in_progress(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        order_number = main_page.create_order()

        main_page.go_to_order_feed()

        assert OrderFeedPage(logged_in_driver).is_order_in_progress(order_number)
