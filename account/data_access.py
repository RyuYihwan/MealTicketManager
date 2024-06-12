import json

from account.account import Account


class DataAccess:
    def __init__(self, data_path):
        self._data_path = data_path

    def get_accounts(self):
        with open(self._data_path, 'r') as f:
            accounts = json.load(f).get('account')
            return accounts

    def add_account(self, account):
        accounts = self.get_accounts()
        json_account = account.__dict__
        accounts.append(json_account)
        with open(self._data_path, 'w') as f:
            json.dump({'account': accounts}, f)

    def get_account_by_username(self, username):
        accounts = self.get_accounts()
        for dict_account in accounts:
            if dict_account['username'] == username:
                account = Account(**dict_account)
                print(account.__dict__)
                return account

