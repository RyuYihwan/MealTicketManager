class OrderTemplate:
    def check_order(self, selected_menu):
        order_response = input(f'금액은 {selected_menu.get("food_price")}입니다. 주문 하시겠습니까? 주문 하시려면 1번, 아니면 2번을 눌러주세요.')

        return order_response

    def order_complete(self, new_order):
        print(f'결제 금액은 {new_order.ordered_price} 입니다. 주문이 완료 되었습니다. 감사합니다.')
