from account.account import Account
from account.constants import Roles


def sign_in(username: str, password: str):
    pass


# 회원 가입
def sign_up(username: str, password: str, role: Roles):

    

    new_account = Account(username, password, role)


    # dbhandler().save(new_account)

    print('회원가입이 완료되었습니다. - ID: f{username}')
