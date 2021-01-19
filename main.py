from code.algorithms import randomise
import sys, os

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '../classes'))
print(rootDir)
if rootDir not in sys.path:     
    sys.path.append(rootDir)

from district import District
from connections import Connections


if __name__ == "__main__":

    # check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py [district]")
        exit(1)
    infile = sys.argv[1]
    district = District(infile)

# --------------------------- Random reassignment --------------------------

randomise.random_assignment(district)
