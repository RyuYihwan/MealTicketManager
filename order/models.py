import uuid


class Order:
    """
    주문 클래스
    """

    def __init__(self, order_id: str, ordered_time: str, ordered_price: int, food_name: str, account_id, restaurant_id: int, food_id: int):
        self.order_id = order_id
        self.ordered_time = ordered_time
        self.ordered_price = ordered_price
        self.food_name = food_name
        self.account_id = account_id
        self.restaurant_id = restaurant_id
        self.food_id = food_id
