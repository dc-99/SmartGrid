from .classes import district
import numpy
from random import choice
import sys

if __name__ == "__main__":

    # check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py [district]")
        exit(1)
    infile = sys.argv[1]
    district = District(infile)

    for house in district.houses:
        house_x = district.houses[house].x 
        house_y = district.houses[house].y 
        house_id = district.houses[house].id

        # Chooses a random battery from the list of batteries
        connected = False
        while connected == False:
            random_battery = choice(district.batteries)
            if (random_battery.currentcapacity + district.houses[house].maxoutput) <= random_battery.maxcapacity:
                connected = True
                random_battery.currentcapacity = random_battery.currentcapacity + district.houses[house].maxoutput
                battery_x = random_battery.x
                battery_y = random_battery.y
                battery_id = random_battery.id
                district.connections[house] = Connections(house, house_id, battery_id)
                
    district.visualise()
    


    
   
    
       


    