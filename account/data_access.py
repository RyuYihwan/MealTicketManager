import json


class DataAccess:
    def __init__(self, data_path):
        self._data_path = data_path

    def _get_accounts(self):
        with open(self._data_path, 'r') as f:
            accounts = json.load(f)
            return accounts


