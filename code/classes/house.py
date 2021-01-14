class House():
    def __init__(self, uid, x, y, maxoutput):
        self.id = uid
        self.x = x
        self.y = y
        self.maxoutput = maxoutput
        self.houses = self.load_houses(f"data/{district}/{district}houses.csv")

    def load_houses(self, house_file):
            """
            Loads houses from csv file and saves coordinates and maxoutput
            """
            with open(house_file, 'r') as in_file:
                reader = csv.DictReader(in_file)
                counter = 0
                for row in reader:
                    self.houses[counter] = House(counter, int(row['x']), int(row['y']), float(row['maxoutput']))
                    counter += 1

    #         Zie comment Bas: niet nodig om x en y nog in aparte lijsten op te slaan
    
    #         # creates lists for x and y house coordinates
    #         for house in self.houses:
    #             x = self.houses[house].x
    #             y = self.houses[house].y
                
    #             self.houses_x.append(x)
    #             self.houses_y.append(y)