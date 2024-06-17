from account.models import AccountDataAccess
from account.templates import AccountTemplate
from account.views import AccountView
from main.main import MainService


def run():

    # 인스턴스 생성 -> 싱글톤 패턴으로 수정 필요함
    account_data_access = AccountDataAccess('db/account.json')
    account_template = AccountTemplate()

    account_view = AccountView(account_template, account_data_access)

    main = MainService(account_view)
    main.ticket_logic()


if __name__ == '__main__':
    run()
