from uuid import uuid4

from data.models import User


def build_user() -> User:
    suffix = uuid4().hex[:10]
    return User(
        email=f"user_{suffix}@example.com",
        password=f"Pwd_{suffix}",
        name=f"User {suffix}",
    )
