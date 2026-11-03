import allure

from pages.main_page import MainPage


@allure.feature("Основная функциональность")
@allure.story("Конструктор")
class TestConstructor:
    @allure.title("При добавлении ингредиента в заказ его счётчик увеличивается")
    def test_adding_ingredient_increases_its_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.get_bun_counter()

        main_page.add_bun_to_order()

        assert main_page.get_bun_counter() > counter_before
