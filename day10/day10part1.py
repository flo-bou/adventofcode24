# puzzle input is a topographic map of the surrounding area
# fill in the missing hiking trails
# a hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1 at each step (a good hiking trail is as long as possible)
# A trailhead is any position that starts one or more hiking trails (heigth 0)
# a trailhead's score is the number of different 9-height positions reachable from that trailhead via a hiking trail
# What is the sum of the scores of all trailheads


# lire le fichier input et le mettre dans une variable
# lire les données et pour chaque 0, lancer une detection:
# lire les cases adjacentes et chercher les +1
# pour chaque +1, recommencer à lire les cases adjacentes
# (utiliser des for pour chacune des hauteurs qui va regrouper tous les chemins possibles)
# quand les 9 sont atteints, stocker les positions dans un set
# la longueur du set est le score de ce trailhead
