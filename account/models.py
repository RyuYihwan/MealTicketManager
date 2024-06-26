import json


class Account:
    """
    계정 데이터 클래스
    """

    def __init__(self, account_id: str, username: str, password: str, money: int, role: int):
        self.account_id = account_id
        self.username = username
        self.password = password
        self.money = money
        # Enum value 로 생성
        self.role = role


class AccountDataAccess:
    """
    계정 데이터 접근 클래스
    """

    def __init__(self, data_path):
        self.data_path = data_path

    def get_accounts(self):
        with open(self.data_path, 'r') as f:
            accounts = json.load(f).get('account')
            return accounts

    # 일단 임시 데이터이므로 불러오고 덮어 쓰기 형태로 진행함.
    # json 형태로 이어쓰기 X
    def add_account(self, account):
        accounts = self.get_accounts()
        json_account = account.__dict__
        accounts.append(json_account)
        with open(self.data_path, 'w') as f:
            json.dump({'account': accounts}, f, indent=4)

    def get_account_by_username(self, username):
        accounts = self.get_accounts()
        for dict_account in accounts:
            if dict_account['username'] == username:
                account = Account(**dict_account)
                return account

    def get_account_money(self, account_id):
        accounts = self.get_accounts()
        for dict_account in accounts:
            if dict_account['account_id'] == account_id:
                return dict_account['money']

    def set_account_money(self, account_id, money):
        accounts = self.get_accounts()
        for dict_account in accounts:
            if dict_account['account_id'] == account_id:
                dict_account['money'] = money

        with open(self.data_path, 'w') as f:
            json.dump({'account': accounts}, f, indent=4)