class Restaurant:
    """
    식당 클래스
    """
    def __init__(self, restaurant_id: str, name: str, show_menu: bool, menu):
        self.restaurant_id = restaurant_id
        self.name = name
        self.show_menu = show_menu
        self.menu = menu


class Menu:
    """
    (임시) 메뉴 클래스
    추후 테이블 설정과
    dict -> Object 변환을 위함.
    """

    