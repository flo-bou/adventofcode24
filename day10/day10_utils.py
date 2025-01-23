import copy


def get_adjacent_positions(position: tuple[int, int]) -> list[tuple[int, int]]:
    """Obtenir les positions ajacentes à la position en entrée

    Args:
        position (tuple[int, int]): Position de la forme (ligne, col)

    Returns:
        list[tuple]: Une liste des (2 à 4) positions (sous forme de tuple (x, y)) adjacentes dans l'ordre Nord, Est, Sud, Ouest. Si la position adjacente est hors de la map, elle n'est pas renvoyée
    """
    results: list = list()
    # North :
    if position[0]-1 >= 0:
        results.append((position[0]-1, position[1]))
    # East :
    if position[1]+1 <= 46:
        results.append((position[0], position[1]+1))
    # South :
    if position[0]+1 <= 46:
        results.append((position[0]+1, position[1]))
    # West :
    if position[1]-1 >= 0:
        results.append((position[0], position[1]-1))
    return results


def get_position_value(position: tuple[int, int], topo_map: list[str]) -> int:
    """Lit la valeur de la carte topographique en entrée à la position donnée

    Args:
        position (tuple[int, int]): Position à lire
        topo_map (list[str]): La carte topographique à utiliser

    Returns:
        int: Valeur numérique lue.
    """
    return int(topo_map[position[0]][position[1]])


def get_incremental_paths(path: list[tuple], topo_map: list[str]) -> list[list]:
    """À partir d'un chemin en entrée, renvoie les (0 à 3) chemins plus longs d'une position dont la hauteur vaut +1 par rapport à la dernière hauteur

    Args:
        path (list[tuple]): Liste des positions (ligne, colonne)
        topo_map (list[str]): La carte topographique à utiliser

    Returns:
        list[list]: Les 0 à 3 chemins corrects
    """
    results: list[list] = list()
    if len(path) > 0:
        last_position_value: int = get_position_value(path[-1], topo_map)
        adjacent_positions: list[tuple] = get_adjacent_positions(path[-1])
        for pos in adjacent_positions:
            if get_position_value(pos, topo_map) == last_position_value+1:
                new_path: list[tuple] = path.copy()
                new_path.append(pos)
                results.append(new_path)
    return results


def get_hiking_trails(initial_position: tuple[int, int], topo_map: list[str]) -> list[list]:
    """Récupère une position de départ et renvoie tous les hiking trails complets

    Args:
        initial_position (tuple[int]): Position de départ. La valeur dans la topo_map devrait être "0"
        topo_map (list[str]): La carte topographique à utiliser

    Returns:
        list[list]: Les hikings trails complets. Un hiking trail est une liste de tuples représentant des positions (ligne, colonne)
    """
    results: list[list] = list()
    paths: list[list] = list()
    new_paths: list[list] = [[initial_position]]
    for height in range(0, 10):
        paths = copy.deepcopy(new_paths)
        if len(paths) == 0:
            break
        new_paths = list()
        for path in paths:
            incremental_paths: list[list] = get_incremental_paths(path, topo_map)
            if len(incremental_paths) > 0:
                new_paths.extend(incremental_paths)
    results = paths
    return results


def get_trailhead_score(hiking_trails: list[list]) -> int:
    """Détecte le nombre de sommets différents atteints par les hiking_trails en entrée (les trailheads/départs doivent être identiques).

    Args:
        hiking_trails (list[list]): Liste des hikings trails (chemins ascendants de 9 cases).

    Returns:
        int: Trailhead score.
    """
    last_positions: set[tuple] = set()
    for trail in hiking_trails:
        last_positions.add(trail[-1])
    print("Pour la position", hiking_trails[0][0] ,", le trailhead score est", len(last_positions))
    return len(last_positions)
