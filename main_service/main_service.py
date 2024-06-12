from account.data_access import DataAccess as AccountDataAccess
from restaurant.data_access import DataAccess as RestaurantDataAccess
from account.service import Service as AccountService
from restaurant.service import Service as RestaurantService
from account.account import Account
from account.constants import Roles
from account.exceptions import AccountNotFound, PasswordNotMatched
from main_service.constants import INITIAL_MESSAGE, Select, MANAGER_MODE_MESSAGE, NORMAL_MODE_MESSAGE, \
    SelectManagerMode, DEVELOPMENT_NOT_COMPLETED_MESSAGE
from utils.time_utils import TimeUtils


class MainService:
    def __init__(self):
        self.account_service = AccountService(AccountDataAccess('./data/account.json'))
        self.restaurant_service = RestaurantService(RestaurantDataAccess('./data/restaurant.json'))
        print('main_service initialized')

    def ticket_logic(self):
        print('프로그램을 시작합니다.')
        # 테스트 항목
        restaurant = self.restaurant_service.get_restaurants()
        print(restaurant)
        time = TimeUtils.get_current_time()
        print(time)
        meal_time_settings = TimeUtils.get_current_meal_time_settings()
        print(meal_time_settings)
        print(meal_time_settings['BREAKFAST_TIME_START'])

        # 선택 변수 선언 및 초기화
        select = -1

        # 종료 선택 전까지 반복
        while select != Select.EXIT_PROGRAM.value:

            select = int(input(INITIAL_MESSAGE))

            if select == Select.SIGN_IN.value:
                account = self.sign_in()

                # 예외 발생으로 계정이 없다면 다시 처음으로 돌아가도록 continue
                if account is None:
                    continue

                # 로그인 된 계정을 확인하여 역할에 따라 다른 모드 실행
                if account.role == Roles.MANAGER.value:
                    select_manager_mode = int(input(MANAGER_MODE_MESSAGE))

                    if select_manager_mode == SelectManagerMode.MEAL_TIME_SETTING.value:
                        # 현재 세팅된 시간을 출력해주고 바꿀시간 등을 입력받도록 함
                        pass
                    elif select_manager_mode == SelectManagerMode.ADD_RESTAURANT.value:
                        print(DEVELOPMENT_NOT_COMPLETED_MESSAGE)

                elif account.role == Roles.NORMAL.value:
                    select_normal = int(input(NORMAL_MODE_MESSAGE))
                    print(select_normal)

            elif select == Select.SIGN_UP.value:
                self.sign_up()

        print('프로그램을 종료합니다.')

    def sign_up(self):
        username = input('아이디: ')
        password = input('비밀번호: ')

        # 기본적으로 일반회원 가입만 가능한 상태.
        self.account_service.sign_up(username, password, Roles.NORMAL)

    def sign_in(self) -> Account:
        try:
            username = input('아이디: ')
            password = input('비밀번호: ')
            account = self.account_service.sign_in(username, password)

            return account

        except AccountNotFound as e1:
            print(e1)
            print('회원이 아니시면, 회원가입 후 이용해주세요.')
        except PasswordNotMatched as e2:
            print(e2)
            print('회원이 아니시면, 회원가입 후 이용해주세요.')
