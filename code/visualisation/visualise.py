from district import District
import matplotlib.pyplot as plt
import json

def visualise(district):
        """
        Visualises all batteries and houses with connections in a plot
        """
        plt.figure()
        for house in district.houses:
            plt.scatter(district.houses[house].x, district.houses[house].y, color='r')
        
        for battery in district.batteries:
            plt.scatter(district.batteries[battery].x, district.batteries[battery].y, color='b')

        # Loops trough all connections and draws lines between all given points
        for connection in district.connections:
            xlist = [district.houses[connection].x, district.batteries[district.connections[connection].battery_id].x, district.batteries[district.connections[connection].battery_id].x]
            ylist = [district.houses[connection].y, district.houses[connection].y, district.batteries[district.connections[connection].battery_id].y]
            plt.plot(xlist, ylist)
        
        plt.xlabel("x-coordinates")
        plt.ylabel("y-coordinates")
        plt.title("Houses (red) and batteries (blue) in district 1 randomly connected")
        plt.show()

def output():
    data = {}
    data['output'] = []

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)