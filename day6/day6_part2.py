from day6_utils import *

# add 1 obstruction so the guard is stuck in a loop
# not at the guard starting position
# how many positions you can use for the obstruction so the guard get stuck in a loop ?
# essayer toutes les positions
# enregistrer l'emplacement (et la direction) à chaque fois que le garde se cogne. S'il recommence alors il est en boucle.


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
guard_initial_position: tuple[int, int] = get_guard_initial_position(initial_map)
guard_initial_direction: str = 'North'

# obtenir les positions d'obstructions à utiliser (inutile de tester avec des positions par lesquelles le garde ne passe pas de base)
scout_guard: Guard = Guard(guard_initial_position, guard_initial_direction, initial_map)
scout_guard.travel()
obstruction_positions: list[tuple] = list(scout_guard.positions_traveled)
obstruction_positions.remove(guard_initial_position)
print("Nombre de positions d'obstructions possibles :", len(obstruction_positions))

# pour chaque position d'obstruction possible lancer le déplacement du garde
for obstruction_position in obstruction_positions:
    new_map: list[str] = generate_new_map(initial_map, obstruction_position)
    new_gard: Guard = Guard(guard_initial_position, guard_initial_direction, new_map)
    new_gard.travel()
    # détecter une boucle :
    if new_gard.is_looping:
        loop_position_nb += 1
        # print("Le garde a bouclé avec la position d'obstruction", obstruction_position)
    else:
        no_loop_position_nb += 1

print("Nombre de position qui ne font pas loop le garde :", no_loop_position_nb) #  97
print("Nombre de position qui font loop le garde :", loop_position_nb) # 4549 ?
