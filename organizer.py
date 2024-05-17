import user


class Organizer(user.User):

    def __init__(self, username: str, password: str, email: str) -> None:
        super().__init__(username, password, email)
        self._type_org = None
        self._name = None
        self._id_user = None

    def register(self, type_org: str, name: str, id_user: str) -> None:
        self._type_org = type_org  # type_org puede ser particular (p) o empresa (b)
        self._name = name
        self._id_user = id_user
        self._is_registered = True

    def return_dict(self) -> dict:
        info_dict = {'username': self._username, 'password': self._password, 'email': self._email,
                     'type_org': self._type_org, 'name': self._name, 'id_user': self._id_user,
                     'event_list': self._event_list, 'is_registered': self._is_registered}
        return info_dict
