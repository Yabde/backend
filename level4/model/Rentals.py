from datetime import datetime

from .Cars import Cars
from .Commission import Commission


class Rentals:
    """Class Rentals
    It contains the main part of the logical functions to deal with the problem
    """

    def __init__(self, attributes_dict, data):
        """Constructor

        :param attributes_dict: Dictionnary with all class instances in the Json file
        :param data: DataBase Object to search the Owner's desired Car 
        """

        self.id = attributes_dict["id"]
        self.car_id = attributes_dict["car_id"]
        self.start_date = attributes_dict["start_date"]
        self.end_date = attributes_dict["end_date"]
        self.distance = attributes_dict["distance"]

        self.n_days = self.n_days()

        self.car = data.get_item_by_name_and_id("Cars", self.car_id)

    def n_days(self):
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d')
        return (end_date - start_date).days + 1

    @classmethod
    def get_all(cls, data):
        """Return a list of Rentals Object"""

        rentals = [Rentals(attr, data) for attr in data.data["rentals"]]
        return rentals

    def get_price_fee(self, car_owner):
        """Compute rentals price with fee
        Usage of Class 'Options' to compute additionnal feature

        :params cars_owner: to retrieve 'price_per_day' and 'price_per_km'
        """
        distance = self.distance
        n_days = self.n_days
        price_per_day = car_owner['price_per_day']
        price_per_km = car_owner['price_per_km']
        price = distance * price_per_km

        if n_days > 10:
            price += price_per_day * \
                round(1 + 3*0.9 + 6*0.7 + (n_days-10)*0.5, 3)
        elif n_days > 4:
            price += price_per_day * \
                round(1 + 3*0.9 + (n_days-4)*0.7, 3)
        elif n_days > 1:
            price += price_per_day * \
                round(1 + (n_days-1)*0.9, 3)
        else:
            price += price_per_day
        price = int(price)

        return price

    def type_of_action(self, key):
        if key == 'driver':
            return "debit"
        else:
            return "credit"

    def fill_actions(self, commission):
        action = [{
            "who": key,
            "type": self.type_of_action(key),
            "amount": value
        } for key, value in commission.items()]

        return action

    def get_final_output(self, data):
        """Compute expected result
        Usage of Class 'Commission'

        :param data: Database Object
        """
        price = self.get_price_fee(self.car)
        n_days = self.n_days
        commission = Commission.compute_commission(n_days, price)

        return {
            "id": self.id,
            "actions": self.fill_actions(commission)
        }
