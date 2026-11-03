from collections.abc import Iterator

import pytest

from api.user_client import UserClient
from data.models import User
from helpers.generators import build_user


@pytest.fixture
def user() -> Iterator[User]:
    client = UserClient()
    new_user = client.register(build_user())
    yield new_user
    client.delete(new_user)
    