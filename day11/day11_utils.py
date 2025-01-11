
from json import load, dump

# Ce qu'on cherche c'est ne plus faire l'algo sur chaque pierre à chaque iteration
# faire du cache sur les resultats ? OUI
# écrire dans un fichier de résultat type stone5_child_nb
# écrire un JSON ? OUI !


def read_result_file(stone: int) -> dict:
    data = dict()
    stone: str = str(stone)
    try:
        with open('./day11/results/stone'+stone+'.json', 'r', encoding="utf-8") as json_file:
            data = load(json_file)
        # print("data read from", 'stone'+stone+'.json', data)
    except FileNotFoundError as e:
        # raise e
        # data = dict()
        print('stone'+stone+'.json', "n'existe pas.")
        with open('./day11/results/stone'+stone+'.json', 'w', encoding="utf-8") as json_file:
            pass
        print('stone'+stone+'.json', "créée.")
    return data


def write_result_file(stone: int, results: dict) -> None:
    """Write results in a JSON file for stone N.

    Args:
        stone (int): Number on the stone
        results (dict): Results to write in the file
    """
    stone: str = str(stone)
    with open('./day11/results/stone'+stone+'.json', 'w', encoding="utf-8") as json_file:
        dump(results, json_file, indent=2, sort_keys=True)
    print('./day11/results/stone'+stone+'.json', "written")


def get_results() -> dict:
    all_known_results: dict = dict() # pour une stone, on va avoir besoin de tous les résultats
    for s in range(0, 10):
        all_known_results[s] = read_result_file(s)
    return all_known_results


def store_results(stone: int, until_blink_nb: int) -> None:
    """Stocke les résultats de stone jusqu'au blink blink_nb. Lit les résultat déjà stocké pour générer plus vite les résultats

    Args:
        stone (int): Nombre sur la pierre
        until_blink_nb (int): Nombre de blinks jusqu'auquel on veut stocker les résultats
    """
    data: dict = dict() # data calculated for stone
    stone_child_nb: int
    # lire les résultats précédents :
    all_known_results: dict = get_results() # pour une stone, on va avoir besoin de tous les résultats
    # lancer le calcul
    for blink_no in range(20, until_blink_nb+1):
        stone_child_nb: int = get_1digit_stone_child_nb(stone, blink_no, all_known_results)
        data[str(blink_no)] = stone_child_nb
        print("Pour le blink", blink_no, "la pierre", str(stone), "génère", str(stone_child_nb), "pierres.")
    # fusionner les 2 :
    data.update(all_known_results[stone])
    # écrire les résultats :
    write_result_file(stone, data)


def get_next_stones(stone: int) -> list[int]:
    # pour 1 blink
    next_stones: list = list()
    stone_str: str = str(stone)
    if stone == 0:
        next_stones.append(1)
    elif len(stone_str)%2 == 0:
        half_length: int = int(len(stone_str)/2)
        next_stones.append(int(stone_str[:half_length]))
        next_stones.append(int(stone_str[half_length:])) # heading 0 retirés
    else:
        next_stones.append(stone*2024)
    return next_stones


# Je vais quand même devoir faire des itérations
# Je lis les stones et quand c'est un single digit, je le retire de la liste et j'appelle get_1-digit_stone_child_nb()
# puis je relance une itération sur la liste réduite
# il faut faire en sorte que le blink de base s'interface bien avec les get_stoneN_child_nb(iter_nb)
# on n'appelle jamais de liste ? Si : pour chaque itération on va calculer les résultats des 1digits (avec cache) puis on va calculer et stocker dans une liste les 2+digits. Puis on passe le tout à la gen suivante.
def blink_opti(stones: list[int], stones_acc: int, blink_remaining: int):
    """Calcule le nombre de pierres générées à partir de stones et stones_acc pour le nombre blink_remaining de blinks restants

    Args:
        stones (list[int]): Liste des pierres, identifiés par le nombre inscrit dessus
        stones_acc (int): Accumulateur  (somme temporaire) des pierres enfants générées
        blink_remaining (int): Nombre de blinks restants à effectuer

    Returns:
        list[int], int: 2 donnés : une liste de pierres présentes dans la prochaine génération et une somme temporaire de pierres qui seront présentes lors du dernier blink
    """
    next_stones: list[int] = list()
    # stones_nb: int = stones_acc
    all_known_results: dict = get_results()
    for stone in stones:
        if stone < 10:
            stones_acc += get_1digit_stone_child_nb(stone, blink_remaining, all_known_results)
        else:
            next_stones.extend(get_next_stones(stone))
    return next_stones, stones_acc


def get_1digit_stone_child_nb(stone: int, iter_nb: int, all_known_results: dict) -> int:
    """Calcule et renvoie le nombre de pierres après iter_nb blinks sur la pierre stone

    Args:
        stone (int): Chiffre (et non nombre) sur la pierre
        iter_nb (int): Nombre d'itérations pour lequel on cherche ce résultat
        all_known_results (dict): Ensemble des résultats déjà trouvés (pour chaque pierre.) Les résultats pour chaque pierre sont dans les clés all_known_results[i] ou i est un entier

    Returns:
        int: Nombre de pierres enfants au bout des iter_nb blinks
    """
    stone_nb: int = 0
    match stone:
        case 0:
            stone_nb = get_stone0_child_nb(iter_nb, all_known_results)
        case 1:
            stone_nb = get_stone1_child_nb(iter_nb, all_known_results)
        case 2:
            stone_nb = get_stone2_child_nb(iter_nb, all_known_results)
        case 3:
            stone_nb = get_stone3_child_nb(iter_nb, all_known_results)
        case 4:
            stone_nb = get_stone4_child_nb(iter_nb, all_known_results)
        case 5:
            stone_nb = get_stone5_child_nb(iter_nb, all_known_results)
        case 6:
            stone_nb = get_stone6_child_nb(iter_nb, all_known_results)
        case 7:
            stone_nb = get_stone7_child_nb(iter_nb, all_known_results)
        case 8:
            stone_nb = get_stone8_child_nb(iter_nb, all_known_results)
        case 9:
            stone_nb = get_stone9_child_nb(iter_nb, all_known_results)
        case _:
            print("ERROR :", stone, "is not a 1-digit long")
    return stone_nb


def get_stone0_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 0 (1) (2024) (20 24) (2 0 2 4)
    # on multiplie par 4 toutes les 4 gens ? non
    # on retire 4 iter et on multiplie par 4 non
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 1
    if iter_nb == 3:
        result = 2
    if iter_nb == 4:
        result = 4
    if iter_nb > 4:
        if str(iter_nb) in all_known_results[0].keys():
            result = all_known_results[0][str(iter_nb)]
        else:
            result = get_stone2_child_nb(iter_nb-4, all_known_results)*2 + get_stone0_child_nb(iter_nb-4, all_known_results) + get_stone4_child_nb(iter_nb-4, all_known_results)
    return result


def get_stone1_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 1 (2024) (20 24) (2 0 2 4)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 2
    if iter_nb == 3:
        result = 4
    if iter_nb > 3:
        if str(iter_nb) in all_known_results[1].keys():
            result = all_known_results[1][str(iter_nb)]
        else:
            result = get_stone2_child_nb(iter_nb-3, all_known_results)*2 + get_stone0_child_nb(iter_nb-3, all_known_results) + get_stone4_child_nb(iter_nb-3, all_known_results)
    return result


def get_stone2_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 2 (4048) (40 48) (4 0 4 8)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 2
    if iter_nb == 3:
        result = 4
    if iter_nb > 3:
        if str(iter_nb) in all_known_results[2].keys():
            result = all_known_results[2][str(iter_nb)]
        else:
            result = get_stone4_child_nb(iter_nb-3, all_known_results)*2 + get_stone0_child_nb(iter_nb-3, all_known_results) + get_stone8_child_nb(iter_nb-3, all_known_results)
    return result


def get_stone3_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 3 (6072) (60 72) (6 0 7 2)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 2
    if iter_nb == 3:
        result = 4
    if iter_nb > 3:
        if str(iter_nb) in all_known_results[3].keys():
            result = all_known_results[3][str(iter_nb)]
        else:
            result = get_stone6_child_nb(iter_nb-3, all_known_results) + get_stone0_child_nb(iter_nb-3, all_known_results) + get_stone7_child_nb(iter_nb-3, all_known_results) + get_stone2_child_nb(iter_nb-3, all_known_results)
    return result


def get_stone4_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 4 (8096) (80 96) (8 0 9 6)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 2
    if iter_nb == 3:
        result = 4
    if iter_nb > 3:
        if str(iter_nb) in all_known_results[4].keys():
            result = all_known_results[4][str(iter_nb)]
        else:
            result = get_stone8_child_nb(iter_nb-3, all_known_results) + get_stone0_child_nb(iter_nb-3, all_known_results) + get_stone9_child_nb(iter_nb-3, all_known_results) + get_stone6_child_nb(iter_nb-3, all_known_results)
    return result


def get_stone5_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 5 (10120) (20.482.880) (2048 2880) (20 48 28 80) (2 0 4 8 2 8 8 0)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 1
    if iter_nb == 3:
        result = 2
    if iter_nb == 4:
        result = 4
    if iter_nb == 5:
        result = 8
    if iter_nb > 5:
        if str(iter_nb) in all_known_results[5].keys():
            result = all_known_results[5][str(iter_nb)]
        else:
            result = get_stone2_child_nb(iter_nb-5, all_known_results)*2 + get_stone0_child_nb(iter_nb-5, all_known_results)*2 + get_stone4_child_nb(iter_nb-5, all_known_results) + get_stone8_child_nb(iter_nb-5, all_known_results)*3
    return result


def get_stone6_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 6 (12144) (24.579.456) (2457 9456) (24 57 94 56) (2 4 5 7 9 4 5 6)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 1
    if iter_nb == 3:
        result = 2
    if iter_nb == 4:
        result = 4
    if iter_nb == 5:
        result = 8
    if iter_nb > 5:
        if str(iter_nb) in all_known_results[6].keys():
            result = all_known_results[6][str(iter_nb)]
        else:
            result = get_stone2_child_nb(iter_nb-5, all_known_results) + get_stone4_child_nb(iter_nb-5, all_known_results)*2 + get_stone5_child_nb(iter_nb-5, all_known_results)*2 + get_stone7_child_nb(iter_nb-5, all_known_results) + get_stone9_child_nb(iter_nb-5, all_known_results) + get_stone6_child_nb(iter_nb-5, all_known_results)
    return result


def get_stone7_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 7 (14168) (28.676.032) (2867 6032) (28 67 60 32) (2 8 6 7 6 0 3 2)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 1
    if iter_nb == 3:
        result = 2
    if iter_nb == 4:
        result = 4
    if iter_nb == 5:
        result = 8
    if iter_nb > 5:
        if str(iter_nb) in all_known_results[7].keys():
            result = all_known_results[7][str(iter_nb)]
        else:
            result = get_stone2_child_nb(iter_nb-5, all_known_results)*2 + get_stone8_child_nb(iter_nb-5, all_known_results) + get_stone6_child_nb(iter_nb-5, all_known_results)*2 + get_stone7_child_nb(iter_nb-5, all_known_results) + get_stone0_child_nb(iter_nb-5, all_known_results) + get_stone3_child_nb(iter_nb-5, all_known_results)
    return result


def get_stone8_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 8 (16192) (32.772.608) (3277 2608) (32 77 26 8) (3 2 7 7 2 6 16192)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 1
    if iter_nb == 3:
        result = 2
    if iter_nb == 4:
        result = 4
    if iter_nb == 5:
        result = 7
    if iter_nb > 5:
        if str(iter_nb) in all_known_results[8].keys():
            result = all_known_results[8][str(iter_nb)]
        else:
            result = get_stone3_child_nb(iter_nb-5, all_known_results) + get_stone2_child_nb(iter_nb-5, all_known_results)*2 + get_stone7_child_nb(iter_nb-5, all_known_results)*2 + get_stone6_child_nb(iter_nb-5, all_known_results) + get_stone16192_child_nb(iter_nb-5, all_known_results)
    return result


def get_stone9_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 9 (18216) (36.869.184) (3686 9184) (36 86 91 84) (3 6 8 6 9 1 8 4)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 1
    if iter_nb == 3:
        result = 2
    if iter_nb == 4:
        result = 4
    if iter_nb == 5:
        result = 8
    if iter_nb > 5:
        if str(iter_nb) in all_known_results[9].keys():
            result = all_known_results[9][str(iter_nb)]
        else:
            result = get_stone3_child_nb(iter_nb-5, all_known_results) + get_stone6_child_nb(iter_nb-5, all_known_results)*2 + get_stone8_child_nb(iter_nb-5, all_known_results)*2 + get_stone9_child_nb(iter_nb-5, all_known_results) + get_stone1_child_nb(iter_nb-5, all_known_results) + get_stone4_child_nb(iter_nb-5, all_known_results)
    return result


def get_stone16192_child_nb(iter_nb: int, all_known_results: dict = dict()) -> int:
    # 16192 (32772608) (3277 2608) (32 77 26 8) (3 2 7 7 2 6 16192)
    result: int = 1
    if iter_nb == 1:
        result = 1
    if iter_nb == 2:
        result = 2
    if iter_nb == 3:
        result = 4
    if iter_nb == 4:
        result = 7
    if iter_nb > 4:
        result = get_stone3_child_nb(iter_nb-4, all_known_results) + get_stone2_child_nb(iter_nb-4, all_known_results)*2 + get_stone7_child_nb(iter_nb-4, all_known_results)*2 + get_stone6_child_nb(iter_nb-4, all_known_results) + get_stone16192_child_nb(iter_nb-4, all_known_results)
    return result


# ----------------------------------- Truc ----------------------------------- #


def blink(stones: list[int]) -> list[int]:
    # used on part1
    next_stones: list = list()
    for stone in stones:
        stone_str: str = str(stone)
        if stone == 0:
            next_stones.append(1)
        elif len(stone_str)%2 == 0:
            half_length: int = int(len(stone_str)/2)
            # next_stones.extend([int(stone_str[:half_length]), int(stone_str[half_length:])])
            next_stones.append(int(stone_str[:half_length]))
            next_stones.append(int(stone_str[half_length:]))
        else:
            next_stones.append(stone*2024)
    return next_stones
