class RestaurantTemplate:

    def choose_restaurant(self, restaurants, meal_time):
        print('등록된 식당 리스트는 다음과 같습니다. ')
        for restaurant in restaurants:
            menus = restaurant.get("menu")
            menus_by_meal_time = menus.get(meal_time)
            menus_list_str = ", ".join(
                f'{menu.get("food_name")}: {menu.get("food_price")}' for menu in menus_by_meal_time
            )
            print(f'{restaurant.get("restaurant_id")}. {restaurant.get("name")}: {menus_list_str}')
        return input('원하시는 식당의 번호를 입력해주세요: ')

    def choose_menu(self, restaurant, meal_time):
        menus = restaurant.get('menu')
        menus_by_meal_time = menus.get(meal_time)

        if restaurant.get("show_menu"):
            print('메뉴가 제공 되는 가게 입니다. 시간 대에 맞는 메뉴가 제공 됩니다.')
            for menu in menus_by_meal_time:
                print(
                    f'{menu.get("food_id")}. {menu.get("food_name")} 가격: {menu.get("food_price")}')

            selected_menu_id = input('원하시는 메뉴의 번호를 입력해주세요: ')

            return menus_by_meal_time[int(selected_menu_id) - 1]

        else:
            print('메뉴가 제공 되지 않는 가게 입니다. 다음 메뉴가 자동 선택 됩니다.')
            menu = menus_by_meal_time[0]
            print(
                f'{menu.get("food_id")}. {menu.get("food_name")} 가격: {menu.get("food_price")}')

            return menu
