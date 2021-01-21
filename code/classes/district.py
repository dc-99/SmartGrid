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


    # def get_house(self, house_id):
    #     house = House.objects.get(id=house_id)

    # def get_battery(self, battery_id):
    #     battery = Battery.objects.get(id=battery_id)

    def load_houses(self, house_file):
        """
        Loads houses from csv file and saves coordinates and maxoutput in House object
        """
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            counter = 0
            for row in reader:
                self.houses[counter] = House(counter, int(row['x']), int(row['y']), float(row['maxoutput']))
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

    # Verplaatsen naar mapje visualisation?
    # def visualise(self):
    #     """
    #     Visualises all batteries and houses with connections in a plot
    #     """
    #     fig=plt.figure()

    #     for house in self.houses:
    #         plt.scatter(self.houses[house].x, self.houses[house].y, color='r')
        
    #     for battery in self.batteries:
    #         plt.scatter(self.batteries[battery].x, self.batteries[battery].y, color='b')

    #     # Loops trough all connections and draws lines between all given points
    #     for connection in self.connections:
    #         xlist = [self.houses[connection].x, self.batteries[self.connections[connection].battery_id].x, self.batteries[self.connections[connection].battery_id].x]
    #         ylist = [self.houses[connection].y, self.houses[connection].y, self.batteries[self.connections[connection].battery_id].y]
    #         plt.plot(xlist, ylist)
    #     plt.xlabel("x-coordinates")
    #     plt.ylabel("y-coordinates")
    #     plt.title("Houses (red) and batteries (blue) in district 1 randomly connected")
    #     plt.show()




    
    
