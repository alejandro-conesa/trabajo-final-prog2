import user


class Organizer(user.User):
    def __init__(self, username: str, password: str, email: str):
        super().__init__(username, password, email)
        self._type_org = None
        self._name = None
        self._id_user = None
        self._event_list = []

    def register(self, type_org: str, name: str, id_user: str):
        self._type_org = type_org
        self._name = name
        self._id_user = id_user