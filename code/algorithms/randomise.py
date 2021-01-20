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
    for battery in district.batteries:
        district.batteries[battery].currentcapacity = 0.0

    for house in district.houses:
        connected = False
        counter = 0 
        while connected == False and counter < maxcount:
            counter += 1
            random_battery = choice(district.batteries)
            if (random_battery.currentcapacity + district.houses[house].maxoutput) <= random_battery.maxcapacity:
                connected = True
                random_battery.currentcapacity = random_battery.currentcapacity + district.houses[house].maxoutput
                battery_id = random_battery.id
                district.connections[house] = battery_id
    return district      
    # district.visualise()

def random_assignment_repeat(district):
    while True:
        random_assignment(district)
        if len(district.connections) == len(district.houses):
            return district

    


    
   
    
       


    
