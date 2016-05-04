__name__ = 'server'


class Server:
    def __init__(self, host, username, password):
        self._host = host
        self._username = username
        self._password = password

    @property
    def host(self):
        return self._host

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
