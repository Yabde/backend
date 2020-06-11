import json


class Options:
    """Class Options"""
    GPS_ppd = 500
    BABY_ppd = 200
    ADDITIONAL_ppd = 1000

    def __init__(self, attributes_dict):
        """Constructor

        :param attributes_dict: Dictionnary with all class instances in the Json file 
        """
        self.id = attributes_dict["id"]
        self.rental_id = attributes_dict["rental_id"]
        self.type_feature = attributes_dict["type"]

    @classmethod
    def get_all(cls, data):
        """Return a list of Options Object"""

        options = [Options(attr) for attr in data.data["options"]]
        return options

    @classmethod
    def get_additionnal_fee(cls, n_days, list_of_type=None):
        """Compute the additionnal feature wanted by the Driver

        :param list_of_type: could be for example ['gps', 'baby_seat']
        :param n_days:
        """
        if list_of_type:
            gps_fee, baby_seat_fee, additional_insurance = 0, 0, 0
            if "gps" in list_of_type:
                gps_fee = Options.GPS_ppd * n_days
            if "baby_seat" in list_of_type:
                baby_seat_fee = Options.BABY_ppd * n_days
            if "additional_insurance" in list_of_type:
                additional_insurance = Options.ADDITIONAL_ppd * n_days

        return gps_fee, baby_seat_fee, additional_insurance
