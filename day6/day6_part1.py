from day6_utils import *

# puzzle input is a map
# the guard is at position '^' (facing up)
# obstruction are shown as '#'
# the patrol protocol is : take a step forward unless an obstruction is directly ahead, in that case, turn rigth (at 90 deg)
# calcul the complete path of the gard, 
# then sum up all the positions he walked on (attention aux doublons)


carte: list = list()

# stocker la carte dans un tableau
with open('./day6/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line: str = input_file.readline()
        if len(line) == 0:
            break
        carte.append(line.strip(' \n'))

# initialisation :
guard_initial_position: list = get_guard_initial_position(carte)
guard_initial_direction: str = 'North'
guard: Guard = Guard(guard_initial_position, guard_initial_direction, carte)
guard.patrolling()

print(len(guard.positions_traveled), "cases différentes parcourues") # 4647 OK
