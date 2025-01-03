# à chaque combinaison, j'ajoute l'inverse
# une chaine de combinaisons c'est sa chaine plus petite + 1 bout avec l'une des 2 possibilités
# de cette manière on peut revenir à une chaine connue, celle de longueur 2 ou 1 puis aller dans l'autre sens


def get_longer_combo(val1: str, val2: str, combinaisons: list) -> list:
    """À partir d'une liste de combinaisons, renvoie toutes les combinaisons avec val1 ou val2 plus longues de 1

    Args:
        val1 (str): Valeur possible dans la combinaison
        val2 (str): Valeur possible dans la combinaison
        combinaisons (list[tuple]): Liste des combinaisons dont on veut obtenir les combinaisons plus longues

    Returns:
        list[tuple]: Liste des combinaisons plus longues de 1
    """
    results: list[tuple] = list()
    for combo in combinaisons:
        results.append(combo+(val1,))
        results.append(combo+(val2,))
    return results


def get_every_combinations(val1: str, val2: str, length: int) -> list[list]:
    """Génère toutes les combinaisons avec les valeurs val1 et val2 de longueur length.
    Par exemple get_every_combinations("A", "B", 2) renvoie [("A","A"),("A","B"),("B","A"),("B","B")]

    Args:
        val1 (str): Valeur possible dans la combinaison
        val2 (str): Valeur possible dans la combinaison
        length (int): Longueur/nombre de valeurs possibles

    Returns:
        list[list]: La liste de toutes les combinaisons de longueur length
    """
    combos: list[list] = list()
    combos.append([])
    combos.append([(val1,), (val2,)])
    for nb in range(2, length):
        combos.append(get_longer_combo(val1, val2, combos[nb-1]))
    return combos


def calculate_operation(val1: int, val2: int, operation: str) -> int:
    """Calcule l'opération avec les valeurs val1 et val2

    Args:
        val1 (int): 1ere opérande
        val2 (int): 2e opérande
        operation (str): Descripteur de l'opération à effectuer. Les 2 valeurs possibles sont "add" pour la somme et "mul" pour la multiplication

    Raises:
        Exception: Levée quand operation n'a pas une valeur autorisée

    Returns:
        int: Le résultat de l'opération
    """
    result: int = None
    if operation == "add":
        result = val1 + val2
    elif operation == "mul":
        result = val1 * val2
    else:
        print("Opération non trouvée.")
        raise Exception
    return result


def try_combinations(target: int, operands: list[int], operators: list) -> int:
    """Teste toutes les combinaisons d'opérateurs sur les opérandes afin de trouver une correspondance avec target.

    Args:
        target (int): Valeur cible à trouver avec les opérations
        operands (list[int]): Liste des opérandes ordonnées
        operators (list[tuple]): Liste des opérateurs ordonnées

    Returns:
        int: La valeur de target si celle-ci a été trouvée, -1 sinon
    """
    result: int = -1
    init: int = operands.pop(0)
    
    for operator in operators:
        pairs: list = list(zip(operator, operands))
        acc: int = init
        for pair in pairs:
            acc = calculate_operation(acc, pair[1], pair[0])
        if acc == target:
            result = target
            print("COMBO FOUND for", target, "using", init, pairs)
            break
    return result
