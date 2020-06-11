import json


class Database():
    """Class Database to acces the data inside the JSON file"""
    FILE_PATH = './data/input.json'

    def __init__(self):
        self._data = Database.load_data(Database.FILE_PATH)

    @staticmethod
    def load_data(file_path):
        with open(file_path) as f:
            return json.load(f)

    @property
    def data(self):
        return self._data

    def get_item_by_name_and_id(self, item_name, item_id, first_match=True):
        """Loap inside a list of dicitionnary
        Used essentially to find the desired owner's Car related to the car_id in 'rentals'

        Note: This method uses directly the json data rather than the array of initialized Objects

        :param item_name: would be either 'Cars', 'Rentals' or 'Options'
        :param item_id:
        :param first_match: If True it will stop on the first element found -> Used to search Owner's Car
        If False it will find all matching occurences -> Used to find 'Options' for additionnal fees : gps, baby_seat...
        """
        if first_match:
            specefic_id_item = next(
                sub_dict for sub_dict in self.data[item_name.lower()] if sub_dict['id'] == item_id)
        else:
            specefic_id_item = [sub_dict["type"]
                                for sub_dict in self.data[item_name.lower()] if sub_dict["rental_id"] == item_id]

        return specefic_id_item
