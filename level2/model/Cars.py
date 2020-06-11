class Cars:
    """Class Car"""

    def __init__(self, attributes_dict):
        """Constructor

        :param attributes_dict: Dictionnary with all class instances in the Json file 
        """
        self.id = attributes_dict["id"]
        self.price_per_day = attributes_dict["price_per_day"]
        self.price_per_km = attributes_dict["price_per_km"]

    @classmethod
    def get_all(cls, data):
        """Return a list of Cars Object"""

        cars = [Cars(attr) for attr in data.data["cars"]]
        return cars
