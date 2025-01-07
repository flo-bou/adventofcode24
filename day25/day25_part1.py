
# the door of CH is locked !
# input is shematics of every lock and key
# The locks are schematics that have the top row filled (#) and the bottom row empty (.); the keys have the top row empty and the bottom row filled.
# locks and keys are made of 5 pins, you can simplify the locks and keys into a list of heights
# if each pin of a key-lock combinaison don't overlap, they fit
# How many unique lock/key pairs fit together without overlapping in any column?

schematic: list[str] = list()
schematics: list[list] = list()


def separate_locks_and_keys(schematics: list[list]) -> tuple[list, list]:
    locks: list[list] = list()
    keys: list[list] = list()
    for schematic in schematics:
        if schematic[0] == "#####":
            locks.append(schematic)
        elif schematic[0] == ".....":
            keys.append(schematic)
        else:
            raise AssertionError
    return (locks, keys)


def transform_schematics_into_heigths(schematics: list[list]) -> list[list]:
    heigths: list[list] = list()
    for schematic in schematics:
        heigth = [0, 0, 0, 0, 0]
        for line in schematic:
            for i, char in enumerate(line):
                if char == "#":
                    heigth[i] += 1
        heigth = list(map(lambda h: h-1, heigth))
        heigths.append(heigth)
    return heigths


def are_fitting(lock: list[int], key: list[int]) -> bool:
    result: bool = True
    for i in range(0, len(lock)):
        if lock[i] + key[i] > 5:
            result = False
            break
    return result


with open('./day25/input.txt', 'r', encoding="utf-8") as input_file:
    while input_file:
        line: str = input_file.readline()
        if line == "":
            break
        elif line == "\n":
            schematics.append(schematic)
            schematic = list()
            continue
        schematic.append(line.strip(' \n'))
print(len(schematics))


locks: list[list] = list()
keys: list[list] = list()
locks, keys = separate_locks_and_keys(schematics)
print(len(locks))
print(len(keys))


locks_heigths: list[list] = transform_schematics_into_heigths(locks)
keys_heigths: list[list] = transform_schematics_into_heigths(keys)
print(locks_heigths)
print(keys_heigths)


pairs_fitting: int = 0
# total_combinations: int = 0
for lock in locks_heigths:
    for key in keys_heigths:
        # total_combinations += 1
        if are_fitting(lock, key):
            pairs_fitting += 1

# print(total_combinations)
print(pairs_fitting) # 2618 OK
