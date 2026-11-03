import allure

from pages.main_page import MainPage


@allure.feature("Основная функциональность")
@allure.story("Окно ингредиента")
class TestIngredientModal:
    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_click_on_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_bun_card()

        assert main_page.is_ingredient_modal_visible()

    @allure.title("Окно с деталями ингредиента закрывается кликом по крестику")
    def test_details_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_bun_card()

        main_page.close_modal()

        assert main_page.is_modal_closed()
