from day8_utils import *
# each antenna is tuned to a specific frequency that one char from a-zA-Z0-9
# input is a map of antennas
# the signal applies at specific antinodes based on the resonant frequencies of the antennas
# an antinode occurs at any point that is perfectly in line with two antennas of the same frequency (on the line formed by the 2 antennas). but only when one of the antennas is twice as far away as the other (a node is in the direction of the other antenna but 2 times farther )
# This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them. (for 2 antennas there is 1 pair so 2 nodes; for 3 antennas, there is 3 pairs so 6 nodes; for 4 antennas, there is 6 pairs so 12 nodes; for 5 antennas, there is 10 pairs ...)
# Antennas with different frequencies don't create antinodes; A and a count as different frequencies.
# antinodes can occur at location with antennas
# antinodes out of map don't count
# how many UNIQUE locations in the map countain an antinode.

def main():
    data: list[str] = list()
    antinodes: set[tuple] = set()

    with open('./day8/input.txt', 'r', encoding="utf-8") as input_file:
        while input_file:
            line: str = input_file.readline()
            if line == "":
                break
            data.append(line.strip(' \n'))

    antennas_map: AntennasMap = AntennasMap(data)
    antennas: dict = antennas_map.detect_antennas()

    for key, val in antennas.items():
        combinations: list[list] = get_pairs_combinations(val)
        for combi in combinations:
            # Pour chaque combinaison, calculer les 2 point de résonnance/antinode et vérifier qu'il est bien sur la map puis le mettre dans un set
            vector: tuple[int, int] = get_vector(*combi)
            possible_antinode1, possible_antinode2 = get_possible_antinodes(combi, vector)
            print("Pour la combinaison", combi, "les antinodes possibles sont", possible_antinode1, possible_antinode2)
            if antennas_map.is_on_map(possible_antinode1):
                antinodes.add(possible_antinode1)
            if antennas_map.is_on_map(possible_antinode2):
                antinodes.add(possible_antinode2)
        print("Après les combinaisons de", key, ",", len(antinodes), "ont été trouvés.")

    # print("Les antinodes sont :", antinodes)
    print("Après toutes les combinaisons,", len(antinodes), "ont été trouvés.") # 295 OK


if __name__ == "__main__":
    main()
