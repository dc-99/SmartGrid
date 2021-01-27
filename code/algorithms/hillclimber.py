from district import District
import copy 


def cable_length(district):
    """
    Calculates total length of all cables between houses and batteries
    """
    cable_length = 0
    for house in district.connections:
        # Checks if house is connected to a house or a battery and calculates length of the connection
        if isinstance(district.connections[house], int):
            house_id = district.connections[house]
            x_distance = abs(district.houses[house].x - district.houses[house_id].x)
            y_distance = abs(district.houses[house].y - district.houses[house_id].y)
        else:
            battery_id = district.connections[house].id
            x_distance = abs(district.houses[house].x - district.batteries[battery_id].x)
            y_distance = abs(district.houses[house].y - district.batteries[battery_id].y)
        cable_length += x_distance + y_distance
    return cable_length


def swapbatteries(district):
    """
    Swaps the batteries of two neighbouring houses if this results in a shorter connection length
    """
    currentstate = copy.deepcopy(district)
    bestlength = cable_length(district)
    for i in range(len(district.connections)):
        for j in range(i+1, len(district.connections)):

            # Swaps the batteries between the houses in the connections dictionary
            temp = currentstate.connections[i]
            currentstate.connections[i] = currentstate.connections[j]
            currentstate.connections[j] = temp

            # Swaps the cables between the houses in House objects
            temp = currentstate.houses[i].cables
            currentstate.houses[i].cables = currentstate.houses[j].cables
            currentstate.houses[j].cables = temp

            currentcapacity = currentstate.connections[i].currentcapacity - currentstate.houses[i].maxoutput + currentstate.houses[j].maxoutput 
            maxcapacity = currentstate.connections[i].maxcapacity

            # Swaps batteries and cables back if swap was invalid
            if currentcapacity > maxcapacity or cable_length(currentstate) > bestlength:
                temp = currentstate.connections[i]
                currentstate.connections[i] = currentstate.connections[j]
                currentstate.connections[j] = temp

                temp = currentstate.houses[i].cables
                currentstate.houses[i].cables = currentstate.houses[j].cables
                currentstate.houses[j].cables = temp

            # Sets bestlength to the current cable_length if it is shorter
            if cable_length(currentstate) < bestlength:
                bestlength = cable_length(currentstate)
    return currentstate

    
def calculate_cost(district):
    """
    Calculates total costs of batteries and cables
    """
    # Creates a list of houses which are connected to the same battery
    all_unique_cables = []
    for battery in district.batteries:
        listofhouses = []

        listofbatteries = district.connections.items()
        for item in listofbatteries:
            if item[1] == district.batteries[battery]:
                listofhouses.append(item[0])

        # Creates a list with coordinates of all cables connected to that battery
        allcables = []
        for house in listofhouses:
            for coordinate in district.houses[house].cables:
                allcables.append(coordinate)
        
        # Removes duplicate coordinates from list of all cables
        unique_cables = list(set(allcables))
        for coordinate in unique_cables:
            all_unique_cables.append(unique_cables)

    # Calculates total cost with battery cost and cable cost
    battery_cost = (len(district.batteries) * 5000)
    cable_cost = (len(all_unique_cables) * 9)
    total_cost = battery_cost + cable_cost
    return total_cost