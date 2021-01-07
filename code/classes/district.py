import csv


class District():
    def __init__(self, district):
        self.load_houses(f"data/{district}/{district}houses.dat")
        

    def load_houses(self, house_file):
        houses = {}

        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                houses[row['id']] = House(row['id'], row['id'])

        return houses

    def load_grid(self):
        dictionary = {}
        s = (10,10)
        grid = numpy.zeros(s, dtype = int)
        return grid
        

