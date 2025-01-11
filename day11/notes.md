CE qu'on cherche c'est ne plus faire l'algo sur chaque pierre à chaque iteration
Trouver les patterns de transformation pour chaque chiffre de départ ?

Patterns :
longueur 10 -> 2 longueur 5-
longueur 8 -> 2 longueur 4- -> 2 longueur 2-
longueur 6 -> 2 longueur 3- -> 2+ longueur 4+
longueur 4 -> 2 longueur 2- -> 4 longueur 1
longueur 2 -> 2 longueur 1

Chercher les boucles :
0 1 2024 (20 24) (2 0 2 4)
1 2024 (20 24) (2 0 2 4) -> nb 1 1 2 4 ou x1 x2 x2 puis relais
2 4048 (40 48) (4 0 4 8)
3 6072 (60 72) (6 0 7 2)
4 8096 (80 96) (8 0 9 6)
5 10120 (20.482.880) (2048 2880) (20 48 28 80) (2 0 4 8 2 8 8 0) OK
6 12144 (24.579.456) (2457 9456) (24 57 94 56) (2 4 5 7 9 4 5 6)
7 14168 (28.676.032) (2867 6032) (28 67 60 32) (2 8 6 7 6 0 3 2)
8 16192 (32.772.608) (3277 2608) (32 77 26 8) (3 2 7 7 2 6 16192)
9 18216 (36.869.184) (3686 9184) (36 86 91 84) (3 6 8 6 9 1 8 4)
16192 (32.772.608) (3277 2608) (32 77 26 08) (3 2 7 7 2 6 0 8)

Il faut chercher les nombres longueur 1 et ne plus les calculer car on connait la longueur qu'ils vont donner à telle itération
Une fois qu'on retombe que sur des trucs connu (ou sur beaucoup), c'est résolvable
Nombres premiers ? non pas du tout

Faire un tableau des chiffres pour stocker les nb de pierre par gen. À chaque gen, on va lire la gen suivante ?

ou alors on va stocker 
