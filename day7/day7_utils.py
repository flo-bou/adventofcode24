# à chaque combinaison, j'ajoute l'inverse
# une chaine de combinaisons c'est sa chaine plus petite + 1 bout avec l'une des 2 possibilités
# de cette manière on peut revenir à une chaine connue, celle de longueur 2 ou 1 puis aller dans l'autre sens


def get_longer_combo(vals: list[str], combinaisons: list[tuple]) -> list[tuple]:
    """À partir d'une liste de combinaisons, renvoie une liste contenant toutes les combinaisons (avec les valeurs de vals) plus longues de 1

    Args:
        vals (list[str]): Liste des valeurs possible dans la combinaison
        combinaisons (list[tuple]): Liste des combinaisons dont on veut obtenir les combinaisons plus longues

    Returns:
        list[tuple]: Liste des combinaisons plus longues de 1
    """
    results: list[tuple] = list()
    for combo in combinaisons:
        for val in vals:
            results.append(combo+(val,))
    return results


def get_every_combinations(vals: list[str], length: int) -> list[list]:
    """Génère toutes les combinaisons avec les valeurs val1 et val2 de longueur length.
    Par exemple get_every_combinations(["A", "B"], 2) renvoie [("A","A"),("A","B"),("B","A"),("B","B")]

    Args:
        vals (list[str]): Liste des valeurs possible dans la combinaison
        length (int): Longueur/nombre de valeurs possibles

    Returns:
        list[list]: La liste de listes contenant toutes les combinaisons de longueur de 0 à length-1. Par exemple l'indice 3 contient une liste de toutes les combinaisons possible de longueur 3.
    """
    combos: list[list] = list()
    combos.append([])
    combos.append([(val,) for val in vals])
    for nb in range(2, length):
        combos.append(get_longer_combo(vals, combos[nb-1]))
    return combos


def calculate_operation(nb1: int, nb2: int, operation: str) -> int:
    """Calcule l'opération avec les valeurs nb1 et nb2

    Args:
        nb1 (int): 1ere opérande
        nb2 (int): 2e opérande
        operation (str): Descripteur de l'opération à effectuer. Les 3 valeurs possibles sont "add" pour la somme, "mul" pour la multiplication et "cat" pour la concaténation

    Raises:
        Exception: Levée quand operation n'a pas une valeur autorisée

    Returns:
        int: Le résultat de l'opération
    """
    result: int
    if operation == "add":
        result = nb1 + nb2
    elif operation == "mul":
        result = nb1 * nb2
    elif operation == "cat":
        result = int(str(nb1) + str(nb2))
    else:
        print("Opération non trouvée.")
        raise Exception
    return result


def try_combinations(target: int, operands: list[int], operator_combinations: list[tuple]) -> int:
    """Teste toutes les combinaisons d'opérateurs sur les opérandes afin de trouver une correspondance avec target.

    Args:
        target (int): Valeur cible à trouver avec les opérations
        operands (list[int]): Liste des opérandes ordonnées
        operators (list[tuple]): Liste de toutes les combinaisons des opérateurs de la longueur adaptée à operands

    Returns:
        int: La valeur de target si celle-ci a été trouvée, -1 sinon
    """
    result: int = -1
    init: int = operands.pop(0)
    acc: int
    
    for operator_combi in operator_combinations:
        pairs: list = list(zip(operator_combi, operands))
        acc = init
        for pair in pairs:
            acc = calculate_operation(acc, pair[1], pair[0])
        if acc == target:
            result = target
            print("MATCHING COMBINATION FOUND for", target, "using", init, pairs)
            break
    return result
