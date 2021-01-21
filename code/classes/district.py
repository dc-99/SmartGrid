import csv
from random import choice
from house import House
from battery import Battery
from connections import Connections
import matplotlib.pyplot as plt

class District():
    def __init__(self, district):
        # NIEUW:
        self.houses = {}
        self.load_houses(f"data/{district}/{district}houses.csv")
        self.batteries = {}
        self.load_batteries(f"data/{district}/{district}batteries.csv")
        self.connections = {}


    def load_houses(self, house_file):
        """
        Loads houses from csv file and saves coordinates and maxoutput in House object
        """
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            counter = 0
            for row in reader:
                self.houses[counter] = House(counter, int(row['x']), int(row['y']), float(row['maxoutput']), [])
                counter += 1


    def load_batteries(self, battery_file):
        """
        Loads batteries from csv file and saves coordinates and capacity in Battery object
        """
        with open(battery_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            # splits position variable in data to separate x and y coordinates
            counter = 0
            for row in reader:
                newposition = row['positie'].split(',')
                currentcapacity = 0.0
                self.batteries[counter] = Battery(counter, int(newposition[0]), int(newposition[1]), float(row['capaciteit']), currentcapacity)
                counter += 1






    
    
