import json

from db.Database import Database
from model.Cars import Cars
from model.Rentals import Rentals

data = Database()

# List of Objects
rentals = Rentals.get_all(data)
# cars = Cars.get_all(data)

file_path = './data/output.json'


def generate_output(file_path):
    rentals_output = {"rentals": []}
    for i in rentals:
        rentals_output["rentals"].append(i.get_final_output(data))

    with open(file_path, 'w') as json_file:
        json.dump(rentals_output, json_file, indent=4)


generate_output(file_path)
