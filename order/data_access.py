import json


class DataAccess:
    def __init__(self, data_path):
        self._data_path = data_path

    def get_orders(self):
        with open(self._data_path, 'r') as f:
            orders = json.load(f).get('order')
            return orders

    # 일단 임시 데이터이므로 불러오고 덮어 쓰기 형태로 진행함.
    # json 형태로 이어쓸 정도로 필요 하지 않음.
    def add_order(self, order):
        orders = self.get_orders()
        json_order = order.__dict__
        orders.append(json_order)
        with open(self._data_path, 'w', encoding='utf-8') as f:
            json.dump({'order': orders}, f, ensure_ascii=False, indent=4)
