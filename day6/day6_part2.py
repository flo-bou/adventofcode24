# add 1 obstruction so the guard is stuck in a loop
# not at the guard starting position
# how many positions you can use for the obstruction so the guard get stuck in a loop ?
# essayer toutes les positions
# enregistrer l'emplacement (et la direction) à chaque fois que le garde se cogne. S'il recommence alors il est en boucle.


def get_guard_initial_position(carte: list[str]) -> list[int]:
    result: list = list()
    for line_index, line in enumerate(carte):
        index = line.find("^")
        if index >= 0:
            result = [line_index, index]
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
    stuck_positions: list[tuple] = list() # list des positions+directions du garde lorsq'il se retrouve en face d'une obstruction (donc après déplacement+changement de direction). Si le garde est de nouveau bloqué au même endoit, on considère qu'il fait une boucle 
    # TODO recheck la direction lors du test
    # stuck_positions_set: set = set()
    guard_position: list = list(guard_initial_position)
    guard_direction: str = guard_initial_direction
    
    # récuperer les positions bloquées (stuck_positions) et trouver les moments où le garde boucle
    # dans ce cas arrêter le déplacement et renvoyer le fait qu'il boucle
    # tant que le garde a une position, cela signifie qu'il n'est pas sorti de la map
    while guard_position != list():
        if tuple([guard_position[0], guard_position[1], guard_direction]) in stuck_positions:
            result = True
            break
        else:
            stuck_positions.append(tuple([guard_position[0], guard_position[1], guard_direction]))
        if guard_direction == 'North':
            guard_position, guard_direction = moving_to_North(test_map, guard_position)
            continue
        if guard_direction == 'East':
            guard_position, guard_direction = moving_to_East(test_map, guard_position)
            continue
        if guard_direction == 'South':
            guard_position, guard_direction = moving_to_South(test_map, guard_position)
            continue
        if guard_direction == 'West':
            guard_position, guard_direction = moving_to_West(test_map, guard_position)
            continue
    return result


initial_map: list[str] = list()
new_line: str = ""
new_map: list[str] = list()
loop_position_nb: int = 0
no_loop_position_nb: int = 0

# stocker la carte dans un tableau
with open('./day6/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line: str = input_file.readline()
        if len(line) == 0:
            break
        initial_map.append(line.strip(' \n'))


# initialisation :
guard_initial_position: list[int] = get_guard_initial_position(initial_map)
guard_initial_direction: str = 'North'


# pour chaque position d'obstruction possible (obstruction_position) (sauf position initiale du garde), lancer le déplacement du garde
for line_index, line in enumerate(initial_map):
    for char_index, char in enumerate(line):
        if [line_index, char_index] == guard_initial_position:
            continue
        new_map = initial_map
        if char_index == len(line)-1: # s'il s'agit du dernier caractèrede la ligne
            new_line = line[:char_index] + "#"
        else:
            new_line = line[:char_index] + "#" + line[char_index+1:]
        new_map[line_index] = new_line
        if is_gard_looping(new_map, guard_initial_position, guard_initial_direction):
            # print("Le garde a bouclé avec la position d'obstruction", line_index, char_index)
            loop_position_nb += 1
        else:
            no_loop_position_nb += 1

print("Nombre de position qui ne font pas loop le garde :", no_loop_position_nb) #  (total 16900)
print("Nombre de position qui font loop le garde :", loop_position_nb) # 3842 FALSE !! 207 ?
