from mainService import MainService
from account.data_access import DataAccess


def run():
    account_data_access = DataAccess('./data/account.json')

    MainService(account_data_access)


if __name__ == '__main__':
    run()
