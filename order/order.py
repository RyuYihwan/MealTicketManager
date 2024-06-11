import uuid


class Order:
    """
    주문 클래스
    """
    def __init__(self, ordered_time):
        self._id = uuid.uuid4()
        self._ordered_time = ordered_time

    # id -> getter만 생성
    @property
    def id(self):
        return self.id

    @property
    def ordered_time(self):
        return self._ordered_time

    @ordered_time.setter
    def ordered_time(self, value):
        self._ordered_time = value

