from account.models import Account
from account.constants import Roles
from account.data_access import AccountDataAccess
from account.exceptions import AccountNotFound, PasswordNotMatched, AccountExisted
from account.services import AccountService
from main_service.constants import INITIAL_MESSAGE, Select, MANAGER_MODE_MESSAGE, NORMAL_MODE_MESSAGE, \
    SelectManagerMode, DEVELOPMENT_NOT_COMPLETED_MESSAGE
from order.data_access import OrderDataAccess
from order.services import OrderService
from restaurant.constants import MenuOption
from restaurant.data_access import RestaurantDataAccess
from restaurant.services import RestaurantService
from utils.time_utils import TimeUtils


class MainService:
    def __init__(self):
        self.account_service = AccountService(AccountDataAccess('./data/account.json'))
        self.restaurant_service = RestaurantService(RestaurantDataAccess('./data/restaurant.json'))
        self.order_service = OrderService(OrderDataAccess('./data/order.json'))

    def ticket_logic(self):
        # 설정 시간 초기화
        TimeUtils.get_current_meal_time_settings()

        # 선택 변수 선언 및 초기화
        select = -1

        # 종료 선택 전까지 반복
        while select != Select.EXIT_PROGRAM.value:

            select = int(input(INITIAL_MESSAGE))

            # 로그인
            if select == Select.SIGN_IN.value:
                account = self.sign_in()

                # 예외 발생 시 계정이 없다면 다시 처음으로 돌아 가도록 continue 실행
                if account is None:
                    continue

                # 로그인 된 계정을 확인 후 역할에 따라 다른 모드 실행
                if account.role == Roles.MANAGER.value:
                    self.manager_mode()

                elif account.role == Roles.NORMAL.value:
                    meal_time = TimeUtils.get_meal_time_from_settings()

                    # 운영시간이 아니라면 break
                    if meal_time == 'breaktime':
                        print('현재는 운영시간이 아닙니다. 관리자에게 문의해주세요.')
                        break

                    self.normal_mode(account.account_id, meal_time)

            # 회원 가입
            elif select == Select.SIGN_UP.value:
                self.sign_up()

    def normal_mode(self, account_id, meal_time):
        print('등록된 식당 리스트는 다음과 같습니다.')
        restaurants = self.restaurant_service.get_restaurants()
        for restaurant in restaurants:
            print(f'{restaurant.get("restaurant_id")}. {restaurant.get("name")}')
        selected_restaurant_id = int(input(NORMAL_MODE_MESSAGE))
        restaurant = self.restaurant_service.get_restaurant_by_id(selected_restaurant_id)
        foods = self.restaurant_service.get_foods_by_id_and_time_settings(selected_restaurant_id,
                                                                          meal_time)
        if restaurant.show_menu == MenuOption.SHOW.value:
            print('메뉴가 제공되는 가게입니다. 메뉴를 선택해 주세요.')
            # 메뉴 출력 및 선택
            for food in foods:
                print(f'{food.get("food_id")}. {food.get("food_name")} 가격: {food.get("food_price")}')
            selected_food_id = int(input("메뉴 번호를 입력해주세요: ")) - 1

            # 원래는 food or menu 테이블 만들어서 가져와야 함.
            selected_food = foods[selected_food_id]

            # 주문
            order_response = int(input(f'금액은 {selected_food.get("food_price")}입니다. 주문 하시겠습니까? 주문 하시려면 1번, 아니면 0번을 눌러주세요.'))
            if order_response:
                self.order_service.add_order(selected_food.get('food_price'), selected_food.get('food_name'),
                                             account_id, selected_restaurant_id, selected_food_id)

                # 결제완료 -> 초기화면
                print(f'결제 금액은 {selected_food.get("food_price")} 입니다. 주문이 완료 되었습니다. 감사합니다.')

        else:
            fixed_food = foods[0]
            fixed_food_id = 1
            print(f'메뉴가 제공되지 않는 가게입니다. 오늘의 메뉴는 {fixed_food.get("food_name")}입니다!')

            # 주문
            order_response = int(input(f'금액은 {fixed_food.get("food_price")}입니다. 주문 하시겠습니까? 주문 하시려면 1번, 아니면 0번을 눌러주세요.'))
            if order_response:
                self.order_service.add_order(fixed_food.get('food_price'), fixed_food.get('food_name'), account_id,
                                             selected_restaurant_id, fixed_food_id)

                # 결제완료 -> 초기화면
                print(f'결제 금액은 {fixed_food.get("food_price")} 입니다. 주문이 완료되었습니다. 감사합니다.')

    def manager_mode(self):
        select_manager_mode = int(input(MANAGER_MODE_MESSAGE))
        if select_manager_mode == SelectManagerMode.MEAL_TIME_SETTING.value:
            # 현재 세팅된 시간을 출력 해주고 변경 시간을 입력 받도록 함 -> 재접속 필요
            self.set_meal_time_by_manager()

        elif select_manager_mode == SelectManagerMode.ADD_RESTAURANT.value:
            print(DEVELOPMENT_NOT_COMPLETED_MESSAGE)

    def set_meal_time_by_manager(self):
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
        try:
            username = input('아이디: ')
            password = input('비밀번호: ')

            # 기본적으로 일반회원 가입만 가능한 상태.
            self.account_service.sign_up(username, password, Roles.NORMAL)
        except AccountExisted as e1:
            print(e1)

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
