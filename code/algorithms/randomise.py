import os, sys
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '../classes'))

import time

if rootDir not in sys.path:     
    sys.path.append(rootDir)

from district import District
from random import choice
import numpy


def random_assignment(district, maxcount=50):
    """
    Connects every house to a random battery with straight connections from house x to battery x and from house y to battery y
    """
    # Initializes an empty connections dictionary and sets the currentcapacity of each battery to zero
    district.connections = {}
    for battery in district.batteries:
        district.batteries[battery].currentcapacity = 0.0

    # Loops through all houses
    for house in district.houses:
        connected = False
        counter = 0 
        x_coordinates = []
        y_coordinates = []
        cables = []
        district.houses[house].cables = cables

        # Chooses random battery until a valid connection is made between a house and battery
        while connected == False and counter < maxcount:
            counter += 1
            random_battery = choice(district.batteries)
            # Saves house id (key) and battery object (value) in connections dictionary if connection is valid
            if (random_battery.currentcapacity + district.houses[house].maxoutput) <= random_battery.maxcapacity:
                connected = True
                random_battery.currentcapacity = random_battery.currentcapacity + district.houses[house].maxoutput
                district.connections[house] = random_battery
            
                # Saves all x and y coordinates of the cable between a house and battery in separate lists
                if district.houses[house].x < random_battery.x:
                    for x_coordinate in range(district.houses[house].x, random_battery.x):
                        x_coordinates.append(x_coordinate)
                else:
                    for x_coordinate in range(random_battery.x, district.houses[house].x):
                        x_coordinates.append(x_coordinate)

                if district.houses[house].y < random_battery.y:
                    for y_coordinate in range(district.houses[house].y, random_battery.y):
                        y_coordinates.append(y_coordinate)
                else: 
                    for y_coordinate in range(random_battery.y, district.houses[house].y):
                        y_coordinates.append(y_coordinate)

        # Combines all x and y coordinates for cable into one cables list and saves it in House object        
        for x in range(len(x_coordinates)):
            coordinates = x_coordinates[x], district.houses[house].y
            cables.append(str(coordinates))
            
        for y in range(len(y_coordinates)):
            coordinates = random_battery.x, y_coordinates[y]
            cables.append(str(coordinates))

        district.houses[house].cables = cables
    return district      


def random_assignment_repeat(district):
    """
    Re-runs random_assignment() function until all houses are connected 
    """
    while True:
        random_assignment(district)
        if len(district.connections) == len(district.houses):
            return district




                



        
    


    

    


    
   
    
       


    
