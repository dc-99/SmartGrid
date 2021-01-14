from code.classes import district, costs
import numpy

if __name__ == "__main__":
    from sys import argv

    # check command line arguments
    if len(argv) != 2:
        print("Usage: python main.py [district]")
        exit(1)
    else:
        district1 = argv[1]
        district.District(district1).visualise()
        costs.Costs(district1).check()
       


    
