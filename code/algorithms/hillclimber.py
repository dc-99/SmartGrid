import random
from district import District
from .randomise import random_assignment
import copy 


def randomSolution(district):
    return random_assignment(district)


def connectionLength(district):
    connectionlength = 0
    for house in district.connections:
        battery_id = district.connections[house]
        x_distance = abs(district.houses[house].x - district.batteries[battery_id].x)
        y_distance = abs(district.houses[house].y - district.batteries[battery_id].y)
        connectionlength += x_distance + y_distance
    return connectionlength


def swapbatteries(district):
    currentstate = copy.deepcopy(district)
    bestlength = connectionLength(district)
    for i in range(len(district.connections)):
        for j in range(i+1, len(district.connections)):
            print(i, j)
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
    battery_cost = (len(district.batteries) * 5000)
    connection_cost = int(bestlength) * 9
    total_cost = battery_cost + connection_cost
    return total_cost