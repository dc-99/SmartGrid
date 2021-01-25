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
    """
    Connects every house to a random battery with straight connections from house x to battery x and from house y to battery y
    """
    district.connections = {}
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
                district.connections[house] = random_battery_id

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


# def combine_connections(district):
#     # Creates a list of houses which are connected to the same battery
#     for battery in district.batteries:
#         listofhouses = []
#         listofbatteries = district.connections.items()
#         for item in listofbatteries:
#             if item[1] == battery:
#                 listofhouses.append(item[0])
        
#         # # Loops through list of houses to compare the coordinates of the cables
#         # counter = len(listofhouses) - 1
#         # for i in range(len(listofhouses)-1):
#         #     j = 0
#         #     for j in range(counter):
#         #         j += i + 1
#         #         cables_i = district.houses[i].cables
#         #         cables_j = district.houses[j].cables
 
#         #     counter -= 1
        
#         allcables = []
#         for house in listofhouses:
#             for coordinate in district.houses[].cables:
#                 allcables.append(coordinate)
#         unique_cables = list(set(allcables))
            


                



        
    


    

    


    
   
    
       


    
