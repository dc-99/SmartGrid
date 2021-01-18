import csv
from random import choice
from house import House
from battery import Battery
from connections import Connections
import matplotlib.pyplot as plt

class District():
    def __init__(self, district):
        self.houses = {}
        self.houses_x = []
        self.houses_y = []
        self.batteries = {}
        self.batteries_x = []
        self.batteries_y = []
        self.connections = {}
        self.load_houses(f"../data/{district}/{district}houses.csv")
        self.load_batteries(f"../data/{district}/{district}batteries.csv")

    """
    def get_house(self, house_id):
        pass 

    def get_battery(self, battery_id):
        pass
    
    """

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

        # creates lists for x and y house coordinates
        for house in self.houses:
            x = self.houses[house].x
            y = self.houses[house].y
            
            self.houses_x.append(x)
            self.houses_y.append(y)


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
                self.batteries_x.append(int(newposition[0]))
                self.batteries_y.append(int(newposition[1]))
                currentcapacity = 0.0
                self.batteries[counter] = Battery(counter, int(newposition[0]), int(newposition[1]), float(row['capaciteit']), currentcapacity)
                counter += 1


    # def make_connections(self):
    #     """
    #     Connects every house to a random battery
    #     """
    #     for house in self.houses:
    #         house_x = self.houses[house].x 
    #         house_y = self.houses[house].y 
    #         house_id = self.houses[house].id

    #         # Chooses a random battery from the list of batteries
    #         connected = False
    #         while connected == False:
    #             random_battery = choice(self.batteries)
    #             if (random_battery.currentcapacity + self.houses[house].maxoutput) <= random_battery.maxcapacity:
    #                 connected = True
    #                 random_battery.currentcapacity = random_battery.currentcapacity + self.houses[house].maxoutput
    #                 battery_x = random_battery.x
    #                 battery_y = random_battery.y
    #                 battery_id = random_battery.id
    #                 self.connections[house] = Connections(house, house_id, battery_id)
                
    # def get_connections(self):
    #     return self.batteries


    def visualise(self):
        """
        Visualises all batteries and houses with connections in a plot
        """
        fig=plt.figure()
        plt.scatter(self.houses_x, self.houses_y, color='r')
        plt.scatter(self.batteries_x, self.batteries_y, color='b')

        # Loops trough all connections and draws lines between all given points
        for connection in self.connections:
            xlist = [self.houses[connection].x, self.batteries[self.connections[connection].battery_id].x, self.batteries[self.connections[connection].battery_id].x]
            ylist = [self.houses[connection].y, self.houses[connection].y, self.batteries[self.connections[connection].battery_id].y]
            plt.plot(xlist, ylist)
        plt.xlabel("x-coordinates")
        plt.ylabel("y-coordinates")
        plt.title("Houses (red) and batteries (blue) in district 1 randomly connected")
        plt.show()
