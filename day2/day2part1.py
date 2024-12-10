# one report per line
# one report is a list of numbers (levels) separated by spaces
# a report is safe if 1. the levels are all increasing/decreasing and 2. two adjacent  differ by at least one and at most 3
# how many reports are safe ?

safe_reports_nb: int = 0

def is_safe(levels: list):
    result: bool = False
    if (sorted(levels) == levels) or (sorted(levels, reverse=True) == levels): # comparaison bonne ?
        # print("Level is ordered")
        for i in range(1, len(levels)):
            result = check_distance(levels[i-1], levels[i])                
            if not result:
                break
    return result


def check_distance(a: int, b: int):
    distance: int = abs(a - b)
    if distance >= 1 and distance <= 3:
        return True
    else:
        return False


# access the local file input.txt
with open('./day2/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line = input_file.readline()
        if len(line) == 0:
            break
        levels = line.strip(' \n').split(' ')
        levels = list(map(lambda nb: int(nb), levels))
        # print(levels)
        if is_safe(levels):
            print("Report is safe :", levels)
            safe_reports_nb += 1
        else:
            print("Report is not safe :", levels)


print("Nombre de reports safes : ", str(safe_reports_nb)) # 463

# access the local input file
# read the file line per line and for each:
    # check if the line/level is in order
        # if true, check the distance between two adjacents numbers is 1 <= nb <= 3 
            # if true add 1 to a counter


