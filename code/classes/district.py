import csv
from .house import House
from .battery import Battery
import matplotlib.pyplot as plt

class District():
    def __init__(self, district):
        self.houses = {}
        self.load_houses(f"data/{district}/{district}houses.csv")
        self.batteries = {}
        self.load_batteries(f"data/{district}/{district}batteries.csv")

    def load_houses(self, house_file):
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            counter = 0
            for row in reader:
                self.houses[counter] = House(counter, row['x'], row['y'], row['maxoutput'])
                counter += 1

    def load_batteries(self, battery_file):
        batteries = {}
        with open(battery_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            counter = 0
            for row in reader:
                self.batteries[counter] = Battery(counter, row['positie'], row['capaciteit'])
                counter += 1

    def load_grid(self):
        dictionary = {}
        s = (10,10)
        grid = numpy.zeros(s, dtype = int)
        return grid

    def visualise(self):
        houses_xdata = []
        houses_ydata = []
        for house in self.houses:
            x = self.houses[house].x
            y = self.houses[house].y
            
            houses_xdata.append(x)
            houses_ydata.append(y)

        batteries_xdata = []
        batteries_ydata = []
        for battery in self.batteries:
            position = self.batteries[battery].position
            newposition = position.split(',')
            batteries_xdata.append(int(newposition[0]))
            batteries_ydata.append(int(newposition[1]))

        fig=plt.figure()
        ax=fig.add_axes([0,0,1,1])
        ax.scatter(houses_xdata, houses_ydata, color='r')
        ax.scatter(batteries_xdata, batteries_ydata, color='b')
        # ax.set_xlabel('x-coordinates')
        # ax.set_ylabel('y-coordinates')
        # ax.set_title('Scatter plot of district')
        plt.show()


        
        


