import random
from district import District
from .randomise import random_assignment, random_assignment_repeat
import copy 


def randomSolution(district):
    return random_assignment_repeat(district)


def connectionLength(district):
    """
    Calculates total lenght of all connections between houses and batteries
    """
    connectionlength = 0
    for house in district.connections:
        battery_id = district.connections[house]
        x_distance = abs(district.houses[house].x - district.batteries[battery_id].x)
        y_distance = abs(district.houses[house].y - district.batteries[battery_id].y)
        connectionlength += x_distance + y_distance
    return connectionlength


def swapbatteries(district):
    """
    Swaps the batteries of two neighbouring houses if this results in a shorter connection length
    """
    currentstate = copy.deepcopy(district)
    bestlength = connectionLength(district)
    for i in range(len(district.connections)):
        for j in range(i+1, len(district.connections)):
            currentstate.connections[i] = district.connections[j]
            currentstate.connections[j] = district.connections[i]

            currentcapacity = currentstate.batteries[currentstate.connections[i]].currentcapacity - currentstate.houses[i].maxoutput + currentstate.houses[j].maxoutput 
            maxcapacity = currentstate.batteries[currentstate.connections[i]].maxcapacity

            if currentcapacity > maxcapacity or connectionLength(currentstate) > bestlength:
                temp = currentstate.connections[i]
                currentstate.connections[i] = currentstate.connections[j]
                currentstate.connections[j] = temp
            
            if connectionLength(currentstate) < bestlength:
                bestlength = connectionLength(currentstate)
    return bestlength

    
def calculate_cost(district, bestlength):
    """
    Calculates total costs of batteries and cables
    """
    battery_cost = (len(district.batteries) * 5000)

    # Check cable coordinates for duplicates and remove these 
    # allcables = []
    # for house in district.houses:
    #     for coordinate in district.houses[house].cables:
    #         allcables.append(coordinate)
    # unique_cables = list(set(allcables))

    # Creates a list of houses which are connected to the same battery
    all_unique_cables = []
    for battery in district.batteries:
        listofhouses = []
        listofbatteries = district.connections.items()
        for item in listofbatteries:
            if item[1] == battery:
                listofhouses.append(item[0])
        
        allcables = []
        for house in listofhouses:
            print(house)
            print(listofhouses)
            for coordinate in district.houses[house].cables:
                allcables.append(coordinate)
        unique_cables = list(set(allcables))
        for coordinate in unique_cables:
            all_unique_cables.append(unique_cables)

    connection_cost = len(all_unique_cables) * 9
    total_cost = battery_cost + connection_cost
    return total_cost