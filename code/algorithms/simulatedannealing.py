from district import District
from .randomise import random_assignment, random_assignment_repeat
from .hillclimber import cable_length, calculate_cost
import random 
import copy
import math


def simulated_annealing(district):
    """ 
    Peforms simulated annealing to find a solution
    """

    initial_temp = 1000.0
    final_temp = 1.0
    alpha = 0.95
    current_temp = initial_temp

    # Initializes current state with district
    currentstate = copy.deepcopy(district)
    solution = currentstate
    length = cable_length(currentstate)
    optimalcost = calculate_cost(currentstate)

    # Loops through connections to find minimum cost
    while current_temp > final_temp:
        for house in currentstate.connections:
            randomhouse = random.choice(currentstate.houses).id
                
            # Swap batteries between house and random house
            temp = currentstate.connections[house]
            currentstate.connections[house] = currentstate.connections[randomhouse] 
            currentstate.connections[randomhouse] = temp
            
            length = cable_length(currentstate)
            cost = calculate_cost(currentstate)

            # Accepts a new optimal cost and solution if cost is smaller
            if cost < optimalcost:
                optimalcost = cost
                solution = currentstate
            else:
                # Calculate the probability of accepting this new currentstate
                delta = optimalcost - cost
                probability = math.exp(-delta / current_temp)

                # Pull a random number between 0 and 1 and see if we accept
                if random.random() < probability:
                    optimalcost = cost
                    solution = currentstate
        # Decreases the temperature
        current_temp = current_temp * alpha
    return solution

def optimalconnections(solution):
    """
    Optimalizes connections by letting houses on the same x or y axis share cables if they are connected to the same battery
    """
    # Creates a list of houses which are connected to the same battery
    for battery in solution.batteries:
        listofhouses = []
        listofbatteries = solution.connections.items()
        for item in listofbatteries:
            if item[1] == solution.batteries[battery]:
                listofhouses.append(item[0])

        # Loops through list of houses 
        counter = len(listofhouses) - 1
        for i in range(len(listofhouses)-1):
            j = 0
            for j in range(counter):
                j += i + 1
                x_coordinate_i = solution.houses[listofhouses[i]].x
                y_coordinate_i = solution.houses[listofhouses[i]].y
                x_coordinate_j = solution.houses[listofhouses[j]].x
                y_coordinate_j = solution.houses[listofhouses[j]].y
    
                xcoordinate_battery = solution.batteries[battery].x
                ycoordinate_battery = solution.batteries[battery].y
                
                x_coordinates = []
                y_coordinates = []
                newcables = []
                
                # Checks if two houses have the same x coordinates
                if x_coordinate_i == x_coordinate_j:
                    diffx_i = abs(xcoordinate_battery - x_coordinate_i)
                    diffx_j = abs(xcoordinate_battery - x_coordinate_j)

                    # Checks if house i is closer to the battery
                    if diffx_i < diffx_j:

                        # Connects house j to house i
                        if y_coordinate_i < y_coordinate_j:
                            for y_coordinate in range(y_coordinate_i + 1, y_coordinate_j):
                                y_coordinates.append(y_coordinate)
                        else: 
                            for y_coordinate in range(y_coordinate_j + 1, y_coordinate_i):
                                y_coordinates.append(y_coordinate)
                        
                        # Converts x and y coordinates to positions 
                        for y in range(len(y_coordinates)):
                            coordinates = x_coordinate_i, y_coordinates[y]
                            newcables.append(str(coordinates))

                        # Saves the new cable coordinates of house j connected to house i
                        solution.houses[listofhouses[j]].cables = newcables
                        solution.connections[listofhouses[j]] = listofhouses[i]
                    else:
                        # Connects house i to house j
                        if y_coordinate_i < y_coordinate_j:
                            for  y_coordinate in range(y_coordinate_i + 1, y_coordinate_j):
                                y_coordinates.append(y_coordinate)
                        else:
                            for y_coordinate in range(y_coordinate_j + 1, y_coordinate_i):
                                y_coordinates.append(y_coordinate)

                        # Converts x and y coordinates to positions 
                        for y in range(len(y_coordinates)):
                            coordinates = x_coordinate_j, y_coordinates[y]
                            newcables.append(str(coordinates))

                        # Saves the new cable coordinates of house i connected to house j
                        solution.houses[listofhouses[i]].cables = newcables    
                        solution.connections[listofhouses[i]] = listofhouses[j]

                # Checks if two houses have the same y coordinates
                if y_coordinate_i == y_coordinate_j:
                    diffy_i = abs(ycoordinate_battery - y_coordinate_i)
                    diffy_j = abs(ycoordinate_battery - y_coordinate_j)

                    # Checks if house i is closer to the battery
                    if diffy_i < diffy_j:

                        # Connects house j to house i 
                        if x_coordinate_i < x_coordinate_j:
                            for x_coordinate in range(x_coordinate_i + 1, x_coordinate_j):
                                x_coordinates.append(x_coordinate)
                        else: 
                            for x_coordinate in range(x_coordinate_j + 1, x_coordinate_i):
                                x_coordinates.append(x_coordinate)
                        
                        # Converts x and y coordinates to positions 
                        for x in range(len(x_coordinates)):
                            coordinates = x_coordinates[x], y_coordinate_i
                            newcables.append(str(coordinates))

                        # Saves the new cable coordinates of house j connected to house i
                        solution.houses[listofhouses[j]].cables = newcables
                        solution.connections[listofhouses[j]] = listofhouses[i]
                    else:
                        # Connects house i to house j
                        if x_coordinate_i < x_coordinate_j:
                            for x_coordinate in range(x_coordinate_i + 1, x_coordinate_j):
                                x_coordinates.append(x_coordinate)
                        else:
                            for x_coordinate in range(x_coordinate_j + 1, x_coordinate_i):
                                x_coordinates.append(x_coordinate)

                        # Convert x and y coordinates to positions 
                        for x in range(len(x_coordinates)):
                            coordinates = x_coordinates[x], y_coordinate_i
                            newcables.append(str(coordinates))

                        # Saves the new cable coordinates of house i connected to house j 
                        solution.houses[listofhouses[i]].cables = newcables
                        solution.connections[listofhouses[i]] = listofhouses[j] 
            counter -= 1
    return solution
