from code.algorithms import randomise, hillclimber
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

district = hillclimber.randomSolution(district)
backupsolution = copy.deepcopy(district)
bestlength = hillclimber.swapbatteries(district)
totalcost = hillclimber.calculate_cost(district, bestlength)
# district.visualise()
print(bestlength, totalcost)

# --------------------------- Visualisation / output -----------------------------------

visualisation.visualise(district)

