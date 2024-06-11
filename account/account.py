from constants import Roles
import uuid


class Account:
    """
    회원 클래스
    """
    def __init__(self, username: str, password: str, role: Roles):
        self._id = uuid.uuid4()
        self._username = username
        self._password = password
        self._role = role

    # id -> getter만 생성
    @property
    def id(self):
        return self.id

    @property
    def username(self):
        return self.username

    @property
    def password(self):
        return self.password

    @property
    def role(self):
        return self.role

    @username.setter
    def username(self, value):
        self._username = value

    @password.setter
    def password(self, value):
        self._password = value

    @role.setter
    def role(self, value):
        self._role = value
