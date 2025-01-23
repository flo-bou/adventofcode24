import day10_utils
# a trailhead rating is the number of distinct hiking trails which began at that trailhead
# What is the sum of the ratings of all trailheads?


def main() -> None:
    topo_map: list[str] = list()
    total_trailhead_rating: int = 0

    # lire le fichier input et le mettre dans une variable
    with open('./day10/input.txt', 'r', encoding="utf-8") as input_file:
        while input_file:
            line: str = input_file.readline()
            if line == "":
                break
            topo_map.append(line.strip(' \n'))


    for line_index, line in enumerate(topo_map):
        for char_index, char in enumerate(line):
            if(char == "0"):
                starting_pos = (line_index, char_index)
                hiking_trails = day10_utils.get_hiking_trails(starting_pos, topo_map)
                print("Hiking trails pour la position", line_index, char_index, ": ", hiking_trails)
                total_trailhead_rating += len(hiking_trails)

    print("Somme des trailhead ratings :", total_trailhead_rating) # 1045 OK


if __name__ == "__main__":
    main()
