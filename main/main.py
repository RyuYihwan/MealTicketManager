from account.views import AccountView


class MainService:
    def __init__(self, account_view: AccountView):
        self.__account_view = account_view

    def ticket_logic(self):
        self.__account_view.sign_in()
