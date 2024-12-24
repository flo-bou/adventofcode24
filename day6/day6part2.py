# add 1 obstruction so the guard is stuck in a loop
# not at the guard starting position
# how many positions you can use for the obstruction so the guard get stuck in a loop ?
# essayer toutes les positions
# enregistrer l'emplacement (et la direction) à chaque fois que le garde se cogne. S'il recommence alors il est en boucle.


def get_guard_initial_position(carte) -> tuple:
    result: tuple = tuple()
    for line_index, line in enumerate(carte):
        index = line.find("^")
        if index >= 0:
            result = (line_index, index)
            break
    return result

# faire des fonctions pour les déplacements E, S, O, N

def moving_to_East(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    # si aucun '#' n'a été atteint, alors le garde est sorti de la carte et final_gard_position vaut []
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
    return final_guard_position, "South"


def moving_to_West(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    # si aucun '#' n'a été atteint, alors le garde est sorti de la carte et final_gard_position vaut []
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
    return final_guard_position, "North"


def moving_to_South(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    # si aucun '#' n'a été atteint, alors le garde est sorti de la carte et final_gard_position vaut []
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
    return final_guard_position, "West"


def moving_to_North(carte: list, guard_position: list):
    # trouver le prochain '#' dans la direction de déplacement du garde
    # si aucun '#' n'a été atteint, alors le garde est sorti de la carte et final_gard_position vaut []
    after_guard: bool = False
    final_guard_position: list = list()
    for line_index, line in reversed(list(enumerate(carte))):
        # trouver la ligne du garde
        if line_index == guard_position[0]:
            after_guard = True
        if after_guard:
            if line[guard_position[1]] == '#': # on va lire une colonne out of range
                final_guard_position = [line_index+1, guard_position[1]]
                break
    return final_guard_position, "East"


# parcours :
def is_gard_looping(test_map: list, guard_initial_position: tuple, guard_initial_direction: str) -> bool:
    result: bool = False
    stuck_positions: list = list()
    guard_position: list = list(guard_initial_position)
    guard_direction: str = guard_initial_direction
    
    # récuperer les positions bloquées (stuck_positions) et trouver les moments où le garde boucle
    # dans ce cas arrêter le déplacment et renvoyer le fait qu'il boucle
    # tant que le garde a une position, cela signifie qu'il n'est pas sorti de la map
    while guard_position != []:
        # print("Guard goes", guard_direction)
        if guard_direction == 'North':
            guard_position, guard_direction = moving_to_North(test_map, guard_position)
            if tuple([guard_position, guard_direction]) in stuck_positions:
                result = True
                break
            else:
                stuck_positions.append((guard_position, guard_direction))
                continue
        if guard_direction == 'East':
            guard_position, guard_direction = moving_to_East(test_map, guard_position)
            if tuple([guard_position, guard_direction]) in stuck_positions:
                result = True
                break
            else:
                stuck_positions.append((guard_position, guard_direction))
                continue
        if guard_direction == 'South':
            guard_position, guard_direction = moving_to_South(test_map, guard_position)
            if tuple([guard_position, guard_direction]) in stuck_positions:
                result = True
                break
            else:
                stuck_positions.append((guard_position, guard_direction))
                continue
        if guard_direction == 'West':
            guard_position, guard_direction = moving_to_West(test_map, guard_position)
            if tuple([guard_position, guard_direction]) in stuck_positions:
                result = True
                break
            else:
                stuck_positions.append((guard_position, guard_direction))
                continue
    
    return result


initial_map: list = list()
new_map: list = list()
loop_position_nb: int = 0

# stocker la carte dans un tableau
with open('./day6/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line: str = input_file.readline()
        if len(line) == 0:
            break
        initial_map.append(line.strip(' \n'))


# initialisation :
guard_initial_position: tuple = get_guard_initial_position(initial_map)
guard_initial_direction: str = 'North'


# pour chaque position d'obstruction possible (obstruction_position) (sauf position initiale du garde), lancer le déplacement du garde
for line_index, line in enumerate(initial_map):
    for char_index, char in enumerate(line):
        if (line_index, char_index) == guard_initial_position:
            continue
        new_map = initial_map
        if char_index == len(line)-1: # s'il s'agit du dernier caractère
            new_line = line[:char_index] + "#"
        else:
            new_line = line[:char_index] + "#" + line[char_index+1:]
        new_map[line_index] = new_line
        if is_gard_looping(new_map, guard_initial_position, guard_initial_direction):
            print("Le garde a bouclé avec la position d'obstruction", line_index, char_index)
            loop_position_nb += 1

print("Nombre de position qui font loop le garde :", loop_position_nb) # 3842 FALSE !!
