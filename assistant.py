import user
from typing import Union


class Assistant(user.User):

    def __init__(self, username: str, password: str, email: str):
        super().__init__(username, password, email)
        self._name = None
        self._birth_date = None
        self._id_num = None
        self._tlf = None
        self._address = None

    def register(self, name: str, birth_date: str, id_num: str, tlf: str, address: dict) -> None:
        self._name = name
        self._birth_date = birth_date
        self._id_num = id_num
        self._tlf = tlf
        self._address = address  # formato {'city': 'Alicante', 'code': '03016', 'street': 'Camino Colonia Romana 20'}
        self._is_registered = True  # solo puedes añadirte a eventos si este valor está en true

    def __str__(self):
        return f'username: {self._username}, password: {self._password}, email: {self._email}\nname: {self._name}, birth date: {self._birth_date}, id: {self._id_num}, tlf: {self._tlf}, address: {self._address}'
