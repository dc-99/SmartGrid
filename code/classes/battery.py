class Battery():
    def __init__(self, uid, x, y, maxcapacity, currentcapacity):
        self.id = uid
        self.x = x
        self.y = y
        self.maxcapacity = maxcapacity
        self.currentcapacity = currentcapacity

        # self.batteries =self.load_batteries(f"data/{district}/{district}batteries.csv")
    
    def load_batteries(self, battery_file):
        """
        Loads batteries from csv file and saves coordinates and capacity in Battery object
        """
        with open(battery_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            # splits position variable in data to separate x and y coordinates
            counter = 0
            for row in reader:
                newposition = row['positie'].split(',')
    
    #             Zie comment Bas: niet nodig om x en y nog in aparte lijsten op te slaan
    #             self.batteries_x.append(int(newposition[0]))
    #             self.batteries_y.append(int(newposition[1]))

                currentcapacity = 0.0
                self.batteries[counter] = Battery(counter, int(newposition[0]), int(newposition[1]), float(row['capaciteit']), currentcapacity)
                counter += 1
