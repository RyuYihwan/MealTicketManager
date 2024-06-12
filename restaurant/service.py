from restaurant.data_access import DataAccess


class Service:
    def __init__(self, data_access: DataAccess):
        self.data_access = data_access

    # # 로그인
    # def sign_in(self, username: str, password: str):
    #     account = self.data_access.find_account_by_username(username)
    #     print(type(account))
    #     if account is None:
    #         raise AccountNotFound()
    #
    #     if account.password != password:
    #         raise PasswordNotMatched()
    #
    #     print(f'로그인 완료: {account.username}')
    #     return account
    #
    # # 회원 가입
    # def sign_up(self, username: str, password: str, role: Roles):
    #     new_account = Account(uuid.uuid4().hex, username, password, role.value)
    #     self.data_access.add_account(new_account)
    #     print(f'회원가입이 완료되었습니다. 로그인 후 이용해주세요. - ID: {username}')

    # 조회
    def get_restaurants(self):
        return self.data_access.get_restaurants()
