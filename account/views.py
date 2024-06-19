from account.constants import Roles
from account.exceptions import AccountException
from account.models import Account, AccountDataAccess
from account.templates import AccountTemplate
from utils.decorators import exception_handler


class AccountView:
    def __init__(self, account_template: AccountTemplate, account_data_access: AccountDataAccess):
        self.__account_template = account_template
        self.__account_data_access = account_data_access

    # 로그인
    @exception_handler
    def sign_in(self):
        sign_in_data = self.__account_template.sign_in()

        account = self.__account_data_access.get_account_by_username(sign_in_data.get('username'))

        if account is None:
            raise AccountException('없는 아이디 입니다.')

        if account.password != sign_in_data.get('password'):
            raise AccountException('비밀 번호가 틀렸습니다.')

        self.__account_template.console_message(f'{account.username} 님이 로그인 하셨습니다.')
        return account

    # 회원 가입
    @exception_handler
    def sign_up(self):
        sign_up_data = self.__account_template.sign_up()
        accounts = self.__account_data_access.get_accounts()
        for account in accounts:
            if account.get('username') == sign_up_data.get('username'):
                raise AccountException('이미 존재 하는 아이디 입니다.')

        # id 부여
        account_id = 1
        if accounts:
            account_id = accounts[-1].get('account_id') + 1

        new_account = Account(account_id, sign_up_data.get('username'), sign_up_data.get('password'), 20000,
                              Roles.NORMAL.value)

        self.__account_data_access.add_account(new_account)

        self.__account_template.console_message('회원가입이 완료되었습니다. 로그인 후 이용해주세요')

    # 조회(테스트용)
    def get_accounts(self):
        return self.__account_data_access.get_accounts()
