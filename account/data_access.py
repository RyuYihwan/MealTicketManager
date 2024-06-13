import json

from account.models import Account


class AccountDataAccess:
    def __init__(self, data_path):
        self.__data_path = data_path

    def get_accounts(self):
        with open(self.__data_path, 'r') as f:
            accounts = json.load(f).get('account')
            return accounts

    # 일단 임시 데이터이므로 불러오고 덮어 쓰기 형태로 진행함.
    # json 형태로 이어쓰기 X
    def add_account(self, account):
        accounts = self.get_accounts()
        json_account = account.__dict__
        accounts.append(json_account)
        with open(self.__data_path, 'w') as f:
            json.dump({'account': accounts}, f, indent=4)

    def get_account_by_username(self, username):
        accounts = self.get_accounts()
        for dict_account in accounts:
            if dict_account['username'] == username:
                account = Account(**dict_account)
                return account

