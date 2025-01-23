import day10_utils
# puzzle input is a topographic map of the surrounding area
# fill in the missing hiking trails
# a hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1 at each step (a good hiking trail is as long as possible)
# A trailhead is any position that starts one or more hiking trails (heigth 0)
# a trailhead's score is the number of different 9-height positions reachable from that trailhead via a hiking trail
# What is the sum of the scores of all trailheads


def main() -> None:
    topo_map: list[str] = list()
    total_trailhead_score: int = 0

    # lire le fichier input et le mettre dans une variable
    with open('./day10/input.txt', 'r', encoding="utf-8") as input_file:
        while input_file:
            line: str = input_file.readline()
            if line == "":
                break
            topo_map.append(line.strip(' \n'))


    # lire les données et pour chaque 0, lancer une detection:
    for line_index, line in enumerate(topo_map):
        for char_index, char in enumerate(line):
            if(char == "0"):
                starting_pos = (line_index, char_index)
                # lire les cases adjacentes et chercher les +1
                # pour chaque +1, recommencer à lire les cases adjacentes
                hiking_trails = day10_utils.get_hiking_trails(starting_pos, topo_map)
                print("Hiking trails pour la position", line_index, char_index, ": ", hiking_trails)
                total_trailhead_score += day10_utils.get_trailhead_score(hiking_trails)

    print("Somme des trailhead score :", total_trailhead_score) # 512 OK


if __name__ == "__main__":
    main()
