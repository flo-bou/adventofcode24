from day11_utils import *

# how many stones afer 75 blinks ?
# problème d'optimisation
# rien que lire une fois la liste c'est long
# pourrait-on connaitre le nombre de pierre sans effectuer le blink ? On veut juste savoir quand la pierre va se diviser
# -> Trouver les patterns de transformation pour chaque chiffre de départ ?
# lire les résultats et 
# ou alors comment ne plus parcourir toute cette liste ? transformer en str ?
# ou alors découper en plus petites listes ? et stocker les résultats entre-temps.
# Prendre le problème pierre par pierre (du début) et chercher des patterns pour simplifier les calculs
# Stocker les résultats dans un fichier ? En faire 10 de suite 50->40
# voir get_stone0 pour un test de simplification

stones: list[int] = list()

with open('./day11/input.txt', 'r+', encoding="utf-8") as input_file:
    while input_file:
        line: str = input_file.readline()
        if line == "":
            break
        stones.extend(list(map(lambda x: int(x), line.strip(' \n').split(" "))))
        print(stones)

next_stones: list[int] = stones
stone_nb_acc: int = 0

for blink_remaining in range(90, 0, -1):
    next_stones, stone_nb_acc = blink_opti(next_stones, stone_nb_acc, blink_remaining)
    print("Il reste", blink_remaining-1, " blinks. Nombre de pierres précalculées :", stone_nb_acc) # 25 -> 198089 OK ; 30 -> 1.604.873 OK ; 35 -> 12.961.338 ; 45 -> 846.491.367 ; 55 -> 55.304.122.209 ; 65 -> 3.614.798.031.580 ; 75 -> 236.302.670.835.517 OK ! ; 90 -> 124.893.218.895.907.126

print("La longueur des next_stones est de", len(next_stones))
print("Le nombre finale de pierres est de", stone_nb_acc+len(next_stones))

# stone1: int = get_stone1_child_nb(25)
# print(stone1)

