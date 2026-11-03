import allure
import requests

from api.base_client import BaseClient
from data import endpoints
from data.models import User


class UserClient(BaseClient):
    @allure.step("Создать пользователя через API")
    def register(self, user: User) -> User:
        response = self.request(
            "POST",
            endpoints.REGISTER,
            json={"email": user.email, "password": user.password, "name": user.name},
        )
        response.raise_for_status()
        user.access_token = response.json()["accessToken"]
        return user

    @allure.step("Удалить пользователя через API")
    def delete(self, user: User) -> requests.Response:
        return self.request(
            "DELETE",
            endpoints.USER,
            headers={"Authorization": user.access_token},
        )
    