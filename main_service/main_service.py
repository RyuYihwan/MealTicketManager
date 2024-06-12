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
        restaurants = self.restaurant_service.get_restaurants()
        print(restaurants)

        restaurant = self.restaurant_service.get_restaurant_by_name('A식당')
        print(restaurant)

        # 설정 시간 초기화
        TimeUtils.get_current_meal_time_settings()

        # 선택 변수 선언 및 초기화
        select = -1

        # 종료 선택 전까지 반복
        while select != Select.EXIT_PROGRAM.value:

            select = int(input(INITIAL_MESSAGE))

            if select == Select.SIGN_IN.value:
                account = self.sign_in()

                # 예외 발생 시 계정이 없다면 다시 처음으로 돌아 가도록 continue 실행
                if account is None:
                    continue

                # 로그인 된 계정을 확인하여 역할에 따라 다른 모드 실행
                if account.role == Roles.MANAGER.value:
                    select_manager_mode = int(input(MANAGER_MODE_MESSAGE))

                    if select_manager_mode == SelectManagerMode.MEAL_TIME_SETTING.value:
                        # 현재 세팅된 시간을 출력 해주고 변경 시간을 입력 받도록 함
                        self.set_meal_time()

                    elif select_manager_mode == SelectManagerMode.ADD_RESTAURANT.value:
                        print(DEVELOPMENT_NOT_COMPLETED_MESSAGE)

                elif account.role == Roles.NORMAL.value:
                    print('등록된 식당 리스트는 다음과 같습니다.')
                    restaurants = self.restaurant_service.get_restaurants()
                    for num, restaurant in enumerate(restaurants, start=1):
                        print(f'{num}. {restaurant["name"]}')
                    selected_restaurant = int(input(NORMAL_MODE_MESSAGE))


            elif select == Select.SIGN_UP.value:
                self.sign_up()

        print('프로그램을 종료합니다.')

    def set_meal_time(self):
        TimeUtils.print_current_meal_time_settings()
        print('시간 형식은 시간:분 형태로 입력해 주세요. ex> 17:20')
        breakfast_time_start = input("BREAKFAST_TIME_START: ")
        breakfast_time_end = input("BREAKFAST_TIME_END: ")
        lunch_time_start = input("LUNCH_TIME_START: ")
        lunch_time_end = input("LUNCH_TIME_END: ")
        dinner_time_start = input("DINNER_TIME_START: ")
        dinner_time_end = input("DINNER_TIME_END: ")
        TimeUtils.set_meal_time_settings(breakfast_time_start, breakfast_time_end, lunch_time_start, lunch_time_end,
                                         dinner_time_start, dinner_time_end)
        TimeUtils.get_current_meal_time_settings()
        TimeUtils.print_current_meal_time_settings()
        print('시간설정이 완료되어 재시작합니다.')

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
