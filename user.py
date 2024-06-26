from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, username: str, password: str, email: str):
        self._username = username
        self._password = password
        self._email = email
        self._event_list: list = []  # lista con los eventos asistidos o creados por un usuario (participante u organizador)

    @abstractmethod
    def register(self, *args) -> None:
        pass

    @abstractmethod
    def return_dict(self) -> dict:
        pass

    def modify_event_list(self, event_list: list) -> None:
        for event in event_list:
            self._event_list.append(event)
