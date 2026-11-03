from dataclasses import dataclass


@dataclass
class User:
    email: str
    password: str
    name: str
    access_token: str = ""
