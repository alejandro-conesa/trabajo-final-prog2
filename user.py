from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email
        self._is_registered = False  # variable que impide participar o crear eventos si está en False

    @abstractmethod
    def register(self, *args):
        pass
