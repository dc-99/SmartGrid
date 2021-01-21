import os, sys
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '../classes'))
print(rootDir)
if rootDir not in sys.path:     
    sys.path.append(rootDir)

from district import District
from connections import Connections
import numpy
import random
from random import choice
 
def random_assignment(district, maxcount=50):
    district.connections = {}
    x = 0
    y = 0
    for battery in district.batteries:
        district.batteries[battery].currentcapacity = 0.0

    for house in district.houses:
        connected = False
        counter = 0 
        x_coordinates = []
        y_coordinates = []
        cables = []
        while connected == False and counter < maxcount:
            counter += 1
            random_battery = choice(district.batteries)
            if (random_battery.currentcapacity + district.houses[house].maxoutput) <= random_battery.maxcapacity:
                connected = True
                random_battery.currentcapacity = random_battery.currentcapacity + district.houses[house].maxoutput
                battery_id = random_battery.id
                district.connections[house] = battery_id

                if district.houses[house].x < random_battery.x:
                    for x_coordinate in range(district.houses[house].x + 1, random_battery.x):
                        x_coordinates.append(x_coordinate)
                else:
                    for x_coordinate in range(random_battery.x + 1, district.houses[house].x):
                        x_coordinates.append(x_coordinate)

                if district.houses[house].y < random_battery.y:
                    for y_coordinate in range(district.houses[house].y + 1, random_battery.y):
                        y_coordinates.append(y_coordinate)
                else: 
                    for y_coordinate in range(random_battery.y + 1, district.houses[house].y):
                        y_coordinates.append(y_coordinate)
                
        for x in range(len(x_coordinates)):
            coordinates = x_coordinates[x], district.houses[house].y
            cables.append(str(coordinates))
        
        for y in range(len(y_coordinates)):
            coordinates = random_battery.x, y_coordinates[y]
            cables.append(str(coordinates))
    
        district.houses[house].cables = cables

    return district      


def random_assignment_repeat(district):
    while True:
        random_assignment(district)
        if len(district.connections) == len(district.houses):
            return district

    


    
   
    
       


    
