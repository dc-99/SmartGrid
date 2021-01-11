from code.classes import district
import numpy

if __name__ == "__main__":
    from sys import argv

    # check command line arguments
    if len(argv) != 2:
        print("Usage: python main.py [district]")
        exit(1)
    else:
        district = argv[1]

    #print(district.District(district))