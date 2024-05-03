import user
from typing import Union

class Assistant(user.User):

    def register(self, name: str, birth_date: str, id: str, tlf: str, address: dict) -> None:
        self._name = name
        self._birth_date = birth_date
        self._id = id
        self._tlf = tlf
        self._address = address  #formato {'city': 'Alicante', 'code': '03016', 'street': 'Camino Colonia Romana 20'}
        self._is_registered = True  # solo puedes añadirte a eventos si este valor está en true
