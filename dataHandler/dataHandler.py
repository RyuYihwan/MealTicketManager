import json


class DataHandler:
    def __init__(self, data_path='../data/db.json'):
        self.data_path = data_path
        self.data = self.data_load()

    def data_load(self):
        with open(self.data_path, 'r') as f:
            # load: json -> python 객체 변환
            data = json.load(f)
            print(data['account'])
            print(data['restaurant'])
            print(data)

    # def data_save(self):
    #     with open(self.data_path, 'w') as f:
    #         # dump: python 객체 -> json 변환 후 저장
    #         json.dump(, f)
