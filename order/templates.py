class OrderTemplate:
    def __init__(self, order_view):
        self.__order_view = order_view

    def add_order(self):

        print('등록된 식당 리스트는 다음과 같습니다.')
        restaurants = self.__restaurant_service.get_restaurants()
        for restaurant in restaurants:
            print(f'{restaurant.get("restaurant_id")}. {restaurant.get("name")}')
        selected_restaurant_id = int(input(NORMAL_MODE_MESSAGE))
        restaurant = self.__restaurant_service.get_restaurant_by_id(selected_restaurant_id)
        foods = self.__restaurant_service.get_foods_by_id_and_time_settings(selected_restaurant_id,
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
            order_response = int(
                input(f'금액은 {selected_food.get("food_price")}입니다. 주문 하시겠습니까? 주문 하시려면 1번, 아니면 0번을 눌러주세요.'))
            if order_response:
                self.__order_service.add_order(selected_food.get('food_price'), selected_food.get('food_name'),
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
                self.__order_service.add_order(fixed_food.get('food_price'), fixed_food.get('food_name'), account_id,
                                               selected_restaurant_id, fixed_food_id)

                # 결제완료 -> 초기화면
                print(f'결제 금액은 {fixed_food.get("food_price")} 입니다. 주문이 완료되었습니다. 감사합니다.')

