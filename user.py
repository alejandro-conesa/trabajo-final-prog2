from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email
        self._event_list: list = []  # lista con los eventos asistidos o creados por un usuario (participante u organizador)
        self._is_registered: bool = False  # variable que impide participar o crear eventos si está en False

    @abstractmethod
    def register(self, *args):
        pass

    @abstractmethod
    def return_dict(self):
        pass
