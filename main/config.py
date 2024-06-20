# 싱글톤 객체 주입 관리
from account.models import AccountDataAccess
from account.templates import AccountTemplate
from account.views import AccountView
from main.main import MainService
from main.templates import MainTemplate
from order.models import OrderDataAccess
from order.templates import OrderTemplate
from order.views import OrderView
from restaurant.models import RestaurantDataAccess
from restaurant.templates import RestaurantTemplate
from restaurant.views import RestaurantView
from utils.decorators import singleton_handler


@singleton_handler
class AppConfig:
    def __init__(self):
        self.__initialize()

    def __initialize(self):
        self.__account_data_access = AccountDataAccess('db/account.json')
        self.__account_template = AccountTemplate()
        self.__account_view = AccountView(self.__account_template, self.__account_data_access)

        self.__restaurant_data_access = RestaurantDataAccess('db/restaurant.json')
        self.__restaurant_template = RestaurantTemplate()
        self.__restaurant_view = RestaurantView(self.__restaurant_template, self.__restaurant_data_access)

        self.__order_data_access = OrderDataAccess('db/order.json')
        self.__order_template = OrderTemplate()
        self.__order_view = OrderView(self.__order_template, self.__order_data_access, self.__account_data_access)

        self.__main_template = MainTemplate()

    def get_main_service(self):
        return MainService(self.__main_template, self.__account_view, self.__restaurant_view, self.__order_view)
