import csv
from .house import House


class District():
    def __init__(self, house_file):
        self.houses = self.load_houses(f"data/{district}/{district}houses.csv")
           
    def load_houses(self, house_file):
        """
        Load all the houses into the district.
        """
        houses = {}

        with open(house_file, 'r') as in_file:

            reader = csv.DictReader(in_file)

            for row in reader:
                nodes[row['id']] = Node(row['id'], row['id'])

        return nodes

    def load_grid(self):
        dictionary = {}
        s = (10,10)
        grid = numpy.zeros(s, dtype = int)
        return grid
        

