import allure

from data import endpoints
from data.models import User
from locators import login_page_locators as locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open_login_page(self) -> None:
        self.open(endpoints.LOGIN_PAGE)

    def login(self, user: User) -> None:
        with allure.step("Войти под пользователем"):
            self.type_text(locators.EMAIL_INPUT, user.email)
            self.type_text(locators.PASSWORD_INPUT, user.password)
            self.click(locators.LOGIN_BUTTON)
            self.wait_invisible(locators.LOGIN_BUTTON)