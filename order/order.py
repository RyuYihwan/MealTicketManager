import uuid


class Order:
    """
    주문 클래스
    """
    def __init__(self, order_id, ordered_time, restaurant_id, menu_id):
        self.order_id = order_id
        self.ordered_time = ordered_time
        self.restaurant_id = restaurant_id
        self.menu_id = menu_id
