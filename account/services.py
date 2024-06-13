from account.models import Account
from account.constants import Roles
from account.data_access import AccountDataAccess
from account.exceptions import AccountNotFound, PasswordNotMatched, AccountExisted


class AccountService:
    def __init__(self, data_access: AccountDataAccess):
        self.data_access = data_access

    # 로그인
    def sign_in(self, username: str, password: str):
        account = self.data_access.get_account_by_username(username)
        if account is None:
            raise AccountNotFound()

        if account.password != password:
            raise PasswordNotMatched()

        print(f'로그인 완료: {account.username}')
        return account

    # 회원 가입
    def sign_up(self, username: str, password: str, role: Roles):
        accounts = self.data_access.get_accounts()
        for account in accounts:
            if account.get('username') == username:
                raise AccountExisted()

        # id 부여
        account_id = 1
        if accounts:
            account_id = accounts[-1].get('account_id') + 1

        new_account = Account(account_id, username, password, role.value)
        self.data_access.add_account(new_account)
        print(f'회원가입이 완료되었습니다. 로그인 후 이용해주세요. - ID: {username}')

    # 조회
    def get_accounts(self):
        return self.data_access.get_accounts()
