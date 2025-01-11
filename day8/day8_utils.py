# faire de l'objet :
# objet map avec les prop contenant la carte
# methode pour détecter les antennas de chaque type et les stocker dans l'objet
# fonction pour générer toutes les paires
# puis pour chaque pair d'antenne du même type
# calculer le vecteur de déplacement de A vers B
# réutiliser ce vecteur pour trouver la position de l'anti-node
# si cet anti-node est bien sur la carte, l'ajouter à la liste des anti-nodes UNIQUES (set ?)


def get_pairs_combinations(values: list[tuple]) -> list[list]:
    """Generate all possible pairs of values from a list of values.

    Args:
        values (list[tuple]): A list of values.

    Returns:
        list[list]: A list of pairs of values.
    """
    pairs_combinations: list[list] = list()
    for value_i in range(0, len(values)):
        if value_i+1 == len(values): # si dernier elem
            continue
        else:
            for value_j in range(value_i+1, len(values)):
                pairs_combinations.append([values[value_i], values[value_j]])
    # print("Pour les valeurs", values, "les combinaisons sont :", pairs_combinations)
    return pairs_combinations


def get_vector(pos1: tuple[int, int], pos2: tuple[int, int]) -> tuple[int, int]:
    # renvoie le vecteur de pos1 vers pos2
    return (pos2[0]-pos1[0], pos2[1]-pos1[1])


def apply_vector_2time(position: tuple[int, int], vector: tuple[int, int]) -> tuple[int, int]:
    """Applies a vector two times to a given position.

    Args:
        position (tuple[int, int]): A tuple of two integers representing the position to apply the vector to.
        vector (tuple[int, int]): A tuple of two integers representing the vector to apply.

    Returns:
        tuple[int, int]: A tuple of two integers representing the new position after applying the vector two times.
    """
    return (position[0]+vector[0]*2, position[1]+vector[1]*2)


def get_possible_antinodes(combination: list[tuple], vector: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    """From a combination of two antennas and a vector between them, it returns the two possible antinodes, by applying the vector two times in both direction.

    Args:
        combination (list[tuple]): A list of two tuples of integers representing the positions of the two antennas.
        vector (tuple[int, int]): A tuple of two integers representing the vector between the two antennas.

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: A tuple of two tuples of integers representing the two possible antinodes.
    """
    antinode1: tuple[int, int] = apply_vector_2time(combination[0], vector)
    vector_neg: tuple[int, int] = (0-vector[0], 0-vector[1])
    # print("Pour la combinaison", combination, "les vecteurs sont :", vector, vector_neg)
    antinode2: tuple[int, int] = apply_vector_2time(combination[1], vector_neg)
    return antinode1, antinode2


class AntennasMap(object):
    """
    Represents a map of antennas.

    Attributes:
        antennas_map (list[str]): A list of strings representing the map of antennas.
        antennas (dict): A dictionary that maps each antenna type (a-zA-Z0-9) to a list of tuples representing the positions of the antennas of that type.

    Methods:
        detect_antennas(): Detects the antennas on the map and populates the `antennas` attribute
        is_on_map(pos: tuple[int, int]): Checks if a given position is on the map.
    """
    def __init__(self, antennas_map: list[str]):
        # super(ClassName, self).__init__()
        self.antennas_map: list[str] = antennas_map
    
    def detect_antennas(self) -> dict:
        """Detects the antennas on the map and populates the `antennas` attribute.
        The `antennas` attribute is a dictionary that maps each antenna type (1 char long amongst a-zA-Z0-9) to a list of tuples representing the positions of the antennas of that type.

        Returns:
            dict: The `antennas` attribute.
        """
        self.antennas: dict = dict()
        for line_i, line in enumerate(self.antennas_map):
            for char_i, char in enumerate(line):
                if char != ".":
                    if char not in self.antennas.keys():
                        self.antennas[char] = []
                    self.antennas[char].append((line_i, char_i))
        # print(self.antennas)
        return self.antennas
        
    def is_on_map(self, pos: tuple[int, int]) -> bool:
        """Checks if a given position is on the map.
        
        Args:
            pos (tuple[int, int]): The position to check.
        
        Returns:
            bool: True if the position is on the map, False otherwise.
        """
        result: bool = True
        if pos[0] < 0 or pos[0] >= len(self.antennas_map):
            result = False
        if pos[1] < 0 or pos[1] >= len(self.antennas_map[0]):
            result = False
        return result


