import csv
from random import choice
from .house import House
from .battery import Battery
from .connections import Connections
import matplotlib.pyplot as plt

class District():
    def __init__(self, district):
        self.houses = {}
        self.houses_x = []
        self.houses_y = []
        self.batteries_x = []
        self.batteries_y = []
        self.load_houses(f"data/{district}/{district}houses.csv")
        self.batteries = {}
        self.connections = {}
        self.load_batteries(f"data/{district}/{district}batteries.csv")

    def load_houses(self, house_file):
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            counter = 0
            for row in reader:
                self.houses[counter] = House(counter, row['x'], row['y'], row['maxoutput'])
                counter += 1

        for house in self.houses:
            x = self.houses[house].x
            y = self.houses[house].y
            
            self.houses_x.append(x)
            self.houses_y.append(y)

    def load_batteries(self, battery_file):
        with open(battery_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            counter = 0
            for row in reader:
                newposition = row['positie'].split(',')
                self.batteries_x.append(int(newposition[0]))
                self.batteries_y.append(int(newposition[1]))
                self.batteries[counter] = Battery(counter, int(newposition[0]), int(newposition[1]), row['capaciteit'])
                counter += 1


    def make_connections(self):
        for house in self.houses:
            house_x = self.houses[house].x 
            house_y = self.houses[house].y 
            house_id = self.houses[house].id

            random_battery = choice(self.batteries)
            battery_x = random_battery.x
            battery_y = random_battery.y
            battery_id = random_battery.id
            
            x_coordinates = []
            y_coordinates = []

            if int(house_x) < int(battery_x):
                for x_coordinate in range((int(house_x) + 1), int(battery_x)):
                    x_coordinates.append(x_coordinate)

            else:
                for x_coordinate in range((int(battery_x) + 1), int(house_x)):
                    x_coordinates.append(x_coordinate)
            
            
            if int(house_y) < int(battery_y):
                for y_coordinate in range((int(house_y) +1), int(battery_y)):
                    y_coordinates.append(y_coordinate)
            
            else: 
                for y_coordinate in range((int(battery_y) +1), int(house_y)):
                    y_coordinates.append(y_coordinate)

            self.connections[house] = Connections(house, house_id, battery_id, x_coordinates, y_coordinates, house_y, battery_y)
        
    def visualise(self):
        fig=plt.figure()
        ax=fig.add_axes([0,0,1,1])
        ax.scatter(self.houses_x, self.houses_y, color='r')
        ax.scatter(self.batteries_x, self.batteries_y, color='b')
        
        self.make_connections()
        for connection in self.connections:
            plt.plot(self.connections[connection].x, self.connections[connection].house_y)
            plt.plot(self.connections[connection].battery_x, self.connections[connection].y)
        
        # ax.set_xlabel('x-coordinates')
        # ax.set_ylabel('y-coordinates')
        # ax.set_title('Scatter plot of district')
        plt.show()