from district import District
from .randomise import random_assignment, random_assignment_repeat
from .hillclimber import connectionLength, calculate_cost
import random 
import copy
import math

def randomstate(district):
    return random_assignment_repeat(district)


def simulated_annealing(district):
    """ 
    Peforms simulated annealing to find a solution
    """

    initial_temp = 50.0
    final_temp = 1.0
    alpha = 0.01

    current_temp = initial_temp

    # Initialize current state with district
    currentstate = copy.deepcopy(district)
    solution = currentstate
    length = connectionLength(currentstate)
    optimalcost = calculate_cost(currentstate, length)

    while current_temp > final_temp:
        for house in currentstate.connections:
            randomhouse = random.choice(currentstate.houses).id
                
            # Swap batteries between house and random house
            temp = currentstate.connections[house]
            currentstate.connections[house] = currentstate.connections[randomhouse] 
            currentstate.connections[randomhouse] = temp

            length = connectionLength(currentstate)
            cost = calculate_cost(currentstate, length)

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
            print(optimalcost)
        # Lower the temperature
        current_temp -= alpha
        print(current_temp)
    # length = connectionLength(solution)
    # print("length:", length, "cost:", calculate_cost(solution, length))
    return solution

def optimalconnections(solution):
    # Creates a list of houses which are connected to the same battery
    for battery in solution.batteries:
        listofhouses = []
        listofbatteries = solution.connections.items()
        for item in listofbatteries:
            if item[1] == battery:
                listofhouses.append(item[0])

        # Loops through list of houses 
        counter = len(listofhouses) - 1
        for i in range(len(listofhouses)-1):
            j = 0
            for j in range(counter):
                j += i + 1


                xcoordinate_i = solution.houses[listofhouses[i]].x
                ycoordinate_i = solution.houses[listofhouses[i]].y
                xcoordinate_j = solution.houses[listofhouses[j]].x
                ycoordinate_j = solution.houses[listofhouses[j]].y
    
                xcoordinate_battery = solution.batteries[battery].x
                ycoordinate_battery = solution.batteries[battery].y
                
                x_coordinates = []
                y_coordinates = []
                newcables = []
                
                # Checks if two houses have the same x coordinates
                if xcoordinate_i == xcoordinate_j:
                    print("test x is hetzelfde")
                    diffx_i = abs(xcoordinate_battery - xcoordinate_i)
                    diffx_j = abs(xcoordinate_battery - xcoordinate_j)

                    # checks which house is closest to battery
                    if diffx_i < diffx_j:

                        # links house that has is futher to battery to house that is near the battery 
                        if listofhouses[i].y < listofhouses[j].y:
                            for y_coordinate in range(listofhouses[i].y + 1, listofhouses[j].y):
                                y_coordinates.append(y_coordinate)
                        else: 
                            for y_coordinate in range(listofhouses[j].y + 1, listofhouses[i].y):
                                y_coordinates.append(y_coordinate)
                        
                        # convert x and y coordinates to positions 
                        for y in range(len(y_coordinates)):
                            coordinates = listofhouses[i].x, y_coordinates[y]
                            newcables.append(str(coordinates))

                        # sets new cables to cables 
                        solution.houses[listofhouses[j]].cables = newcables
                    else:
                        
                        if listofhouses[i].y < listofhouses[j].y:
                            for  y_coordinate in range(listofhouses[i].y + 1, listofhouses[j].y):
                                y_coordinates.append(y_coordinate)
                        else:
                            for y_coordinate in range(listofhouses[j].y + 1, listofhouses[i].y):
                                y_coordinates.append(y_coordinate)

                        # convert x and y coordinates to positions 
                        for y in range(len(y_coordinates)):
                            coordinates = listofhouses[j].x, y_coordinates[y]
                            newcables.append(str(coordinates))

                        # sets new cables to cables 
                        solution.houses[listofhouses[i]].cables = newcables    

                if ycoordinate_i == ycoordinate_j:
                    print("test y is hetzelfde")
                    diffy_i = abs(ycoordinate_battery - ycoordinate_i)
                    diffy_j = abs(ycoordinate_battery - ycoordinate_j)

                    # checks which house is closed to battery
                    if diffy_i < diffy_j:

                        # links house that has is futher to battery to house that is near the battery 
                        if listofhouses[i].x < listofhouses[j].x:
                            for x_coordinate in range(listofhouses[i].x + 1, listofhouses[j].x):
                                x_coordinates.append(x_coordinate)
                        else: 
                            for x_coordinate in range(listofhouses[j].x + 1, listofhouses[i].x):
                                x_coordinates.append(x_coordinate)
                        
                        # convert x and y coordinates to positions 
                        for x in range(len(x_coordinates)):
                            coordinates = x_coordinates[x], listofhouses[i].y
                            newcables.append(str(coordinates))

                        # sets new cables to cables 
                        solution.houses[listofhouses[j]].cables = newcables
                    else:
                        
                        if listofhouses[i].x < listofhouses[j].x:
                            for x_coordinate in range(listofhouses[i].x + 1, listofhouses[j].x):
                                x_coordinates.append(x_coordinate)
                        else:
                            for x_coordinate in range(listofhouses[j].x + 1, listofhouses[i].x):
                                x_coordinates.append(x_coordinate)

                        # convert x and y coordinates to positions 
                        for x in range(len(x_coordinates)):
                            coordinates = x_coordinates[x], listofhouses[i].y
                            newcables.append(str(coordinates))

                        # sets new cables to cables 
                        solution.listofhouses[i].cables = newcables 
            counter -= 1
    return solution
