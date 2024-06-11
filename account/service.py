from account.account import Account
from account.constants import Roles


class Service:
    def __init__(self, data_access):
        self.data_access = data_access

    def sign_in(self, username: str, password: str):
        pass

    # 회원 가입
    def sign_up(self, username: str, password: str, role: Roles):
        new_account = Account(username, password, role)

        print('회원가입이 완료되었습니다. - ID: f{username}')

    # 조회
    def get_accounts(self):
        return self.data_access.get_accounts()
