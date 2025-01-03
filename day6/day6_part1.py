# puzzle input is a map
# the guard is at position '^' (facing up)
# obstruction are shown as '#'
# the patrol protocol is : take a step forward unless an obstruction is directly ahead, in that case, turn rigth (at 90 deg)
# calcul the complete path of the gard, 
# then sum up all the positions he walked on (attention aux doublons)


def get_guard_initial_position(carte):
    result = list()
    for line_index, line in enumerate(carte):
        index = line.find("^")
        if index >= 0:
            result = [line_index, index]
            break
    return result

# faire des fonctions pour les déplacements E, S, O, N


def to_East(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    positions_traveled: set = set()
    after_guard: bool = False
    final_guard_position: list = list()
    for char_index, char in enumerate(carte[guard_position[0]]):
        # trouver la position du garde sur la ligne :
        if char_index == guard_position[1]:
            after_guard = True
            continue
        if after_guard:
            if char == "#":
                final_guard_position = [guard_position[0], char_index-1]
                break
            else:
                positions_traveled.add((guard_position[0], char_index))
    # # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
    # if final_guard_position == []:
    #     final_guard_position = None
    return final_guard_position, "South", positions_traveled


def to_West(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    positions_traveled: set = set()
    after_guard: bool = False
    final_guard_position: list = list()
    for char_index, char in reversed(list(enumerate(carte[guard_position[0]]))):
        # trouver la position du garde sur la ligne :
        if char_index == guard_position[1]:
            after_guard = True
            continue
        if after_guard:
            if char == "#":
                final_guard_position = [guard_position[0], char_index+1]
                break
            else:
                positions_traveled.add((guard_position[0], char_index))
    # # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
    # if final_guard_position == []:
    #     final_guard_position = None
    return final_guard_position, "North", positions_traveled


def to_South(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    positions_traveled: set = set()
    after_guard: bool = False
    final_guard_position: list = list()
    for line_index, line in enumerate(carte):
        # trouver la ligne du garde
        if line_index == guard_position[0]:
            after_guard = True
        if after_guard:
            if line[guard_position[1]] == '#':
                final_guard_position = [line_index-1, guard_position[1]]
                break
            else:
                positions_traveled.add((line_index, guard_position[1]))
    # # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
    # if final_guard_position == []:
    #     final_guard_position = None
    return final_guard_position, "West", positions_traveled


def to_North(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    positions_traveled: set = set()
    after_guard: bool = False
    final_guard_position: list = list()
    for line_index, line in reversed(list(enumerate(carte))):
        # trouver la ligne du garde
        if line_index == guard_position[0]:
            after_guard = True
        if after_guard:
            if line[guard_position[1]] == '#':
                final_guard_position = [line_index+1, guard_position[1]]
                break
            else:
                positions_traveled.add((line_index, guard_position[1]))
    # # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
    # if final_guard_position == []:
    #     final_guard_position = None
    return final_guard_position, "East", positions_traveled


carte: list = list()
positions_traveled: set = set()

# stocker la carte dans un tableau
with open('./day6/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line: str = input_file.readline()
        if len(line) == 0:
            break
        carte.append(line.strip(' \n'))


# guard_position, guard_direction, new_positions_traveled = to_North(carte, guard_position)
# guard_position, guard_direction, new_positions_traveled = to_West(carte, guard_position)
# guard_position, guard_direction, new_positions_traveled = to_South(carte, guard_position)
# guard_position, guard_direction, new_positions_traveled = to_East(carte, guard_position)
# print(len(new_positions_traveled), "cases parcourues")

# initialisation :
guard_position: list = get_guard_initial_position(carte)
positions_traveled.add((guard_position[0], guard_position[1])) # initial position
guard_direction: str = 'North'

# parcours :
while guard_position != []:
    if guard_direction == 'North':
        guard_position, guard_direction, new_positions_traveled = to_North(carte, guard_position)
        positions_traveled = positions_traveled.union(new_positions_traveled)
        continue
    if guard_direction == 'East':
        guard_position, guard_direction, new_positions_traveled = to_East(carte, guard_position)
        positions_traveled = positions_traveled.union(new_positions_traveled)
        continue
    if guard_direction == 'South':
        guard_position, guard_direction, new_positions_traveled = to_South(carte, guard_position)
        positions_traveled = positions_traveled.union(new_positions_traveled)
        continue
    if guard_direction == 'West':
        guard_position, guard_direction, new_positions_traveled = to_West(carte, guard_position)
        positions_traveled = positions_traveled.union(new_positions_traveled)
        continue
    

print(len(positions_traveled), "cases différentes parcourues") # 4647 OK
