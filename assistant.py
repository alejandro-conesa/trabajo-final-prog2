import user


class Assistant(user.User):

    def __init__(self, username: str, password: str, email: str) -> None:
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

    def return_dict(self) -> dict:
        info_dict = {'username': self._username, 'password': self._password, 'email': self._email, 'name': self._name,
                     'birth_date': self._birth_date, 'id_num': self._id_num, 'tlf': self._tlf, 'address': self._address,
                     'event_list': self._event_list, 'is_registered': self._is_registered}
        return info_dict
