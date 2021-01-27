from code.algorithms import randomise, hillclimber, simulatedannealing
from code.visualisation import visualise
import sys, os

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '../classes'))
print(rootDir)
if rootDir not in sys.path:     
    sys.path.append(rootDir)

from district import District
import json


if __name__ == "__main__":

    # check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py [district] [algorithm]")
        exit(1)
    infile = sys.argv[1]
    district = District(infile)

# --------------------------- Random reassignment --------------------------

if sys.argv[2] == "randomise":
    district = randomise.random_assignment_repeat(district)
    # length = hillclimber.cable_length(district)
    totalcost = hillclimber.calculate_cost(district)

# --------------------------- Hillclimber ----------------------------------

if sys.argv[2] == "hillclimber":
    district = randomise.random_assignment_repeat(district)
    currentstate = hillclimber.swapbatteries(district)
    # length = hillclimber.cable_length(currentstate)
    totalcost = hillclimber.calculate_cost(district)

# --------------------------- Simulated annealing ---------------------------

if sys.argv[2] == "simulatedannealing":
    district = randomise.random_assignment_repeat(district)
    solution = simulatedannealing.simulated_annealing(district)
    district = simulatedannealing.optimalconnections(solution)
    # length = hillclimber.cable_length(district)
    totalcost = hillclimber.calculate_cost(district)

# --------------------------- Visualisation / Output -------------------------

visualise.visualise(district)

# Creates json output file 
output = {}
output['output'] = []

if sys.argv[1] == "district_1"
    number = "1"
if sys.argv[1] == "district_2"
    number = "2"
if sys.argv[1] == "district_3"
    number = "3"

output_district = {"district" : number, "costs" : str(totalcost)}
output['output'].append(output_district)

houses = []
output_houses = {}
listofhouses = []
for battery in district.batteries:
    for house in district.connections:
        if district.connections[house] == district.batteries[battery]:
            houses.append(house)
        else:    
            connected = True
            connected_houses = []
            newkey = house
            while connected == True:
                if isinstance(district.connections[newkey], int):
                    connected_houses.append(newkey)
                    newkey = district.connections[newkey] 
                else:
                    connected = False
            
            if district.connections[newkey] == district.batteries[battery]:
                for house in connected_houses:
                    houses.append(house)

    for house in houses:
        location = district.houses[house].x, district.houses[house].y
        output_houses = {
            "location" : str(location),
            "output" : str(district.houses[house].maxoutput),
            "cables" : district.houses[house].cables
        }
        listofhouses.append(output_houses)

    location = district.batteries[battery].x, district.batteries[battery].y
    output_battery = {
        "location" : str(location), 
        "capacity" : str(district.batteries[battery].maxcapacity),
        "houses" : listofhouses
    }

    output['output'].append(output_battery)

with open('output.json', 'w') as outfile:
    json.dump(output, outfile, indent = 4)
