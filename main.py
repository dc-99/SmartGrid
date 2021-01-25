from code.algorithms import randomise, hillclimber, simulatedannealing
from code.visualisation import visualise
import sys, os

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '../classes'))
print(rootDir)
if rootDir not in sys.path:     
    sys.path.append(rootDir)

from district import District
from connections import Connections
import copy
import json


if __name__ == "__main__":

    # check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py [district]")
        exit(1)
    infile = sys.argv[1]
    district = District(infile)

# --------------------------- Random reassignment --------------------------

# randomise.random_assignment(district)

# --------------------------- Hillclimber --------------------------

# district = hillclimber.randomSolution(district)
# backupsolution = copy.deepcopy(district)
# bestlength = hillclimber.swapbatteries(district)
# totalcost = hillclimber.calculate_cost(district, bestlength)
# print(bestlength, totalcost)

# --------------------------- Simulated annealing --------------------------
district = simulatedannealing.randomstate(district)
solution = simulatedannealing.simulated_annealing(district)
simulatedannealing.optimalconnections(solution)

# --------------------------- Visualisation / output -----------------------------------


# visualise.visualise(district)

# data = {}
# data['output'] = []

# output_district = {"district" : str(sys.argv[1]), "costs" : str(totalcost)}
# data['output'].append(output_district)

# houses = []
# output_houses = {}
# listofhouses = []
# for battery in district.batteries:
#     for house in district.connections:
#         if district.connections[house] == battery:
#             houses.append(house)

#     for house in houses:
#         location = district.houses[house].x, district.houses[house].y
#         output_houses = {
#             "location" : str(location),
#             "output" : str(district.houses[house].maxoutput),
#             "cables" : district.houses[house].cables
#         }
#         listofhouses.append(output_houses)

#     location = district.batteries[battery].x, district.batteries[battery].y
#     output_battery = {
#         "location" : str(location), 
#         "capacity" : str(district.batteries[battery].maxcapacity),
#         "houses" : listofhouses
#     }

#     data['output'].append(output_battery)

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile, indent = 4)
