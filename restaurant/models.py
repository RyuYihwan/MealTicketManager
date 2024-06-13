class Restaurant:
    """
    식당 클래스
    """
    def __init__(self, restaurant_id: str, name: str, show_menu: int, menu):
        self.restaurant_id = restaurant_id
        self.name = name
        self.show_menu = show_menu
        self.menu = menu
