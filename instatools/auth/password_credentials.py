import instatools.base.credentials as credentials
import instatools.base.exceptions as exceptions

class PasswordCredentials(credentials.Credentials):
    
    _username = None
    _password = None

    def __init__(self, username, password, payload_formatter=None):
        super(PasswordCredentials, self).__init__(payload_formatter=payload_formatter)

        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        if not isinstance(val, str):
            raise TypeError('The username property must be set to a str')
        if not val:
            raise ValueError('The username property cannot be set to the empty string')
        self._username = val

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        if not isinstance(val, str):
            raise TypeError('The password property must be set to a str')
        if not val:
            raise ValueError('The password property cannot be set to the empty string')
        self._password = val
