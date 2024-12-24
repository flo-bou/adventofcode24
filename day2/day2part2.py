# the problem dampener allows one bad level in a safe report
# if removing 1 bad level from an unsafe report make it safe, then it is safe
# remake the analysis and count the total number of safe reports (including "almost"-safe reports)

# reuse the code from part one and add :
# if the report is unsafe test it again if you remove the 1st level, if not, try to remove the 2nd level, and so on...

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


def is_almost_safe(levels: list):
    result = False
    print("Testing if ", levels, " is almost safe")
    for i, level in enumerate(levels):
        temp_levels = levels.copy()
        removed_level = temp_levels.pop(i)
        # print(temp_levels)
        if is_safe(temp_levels):
            print("Report is safe (after removing '", removed_level, "') :", temp_levels)
            result = True
        else:
            continue
    return result


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
            if is_almost_safe(levels):
                safe_reports_nb += 1
            else:
                print("Report is not safe :", levels)


print("Nombre de reports safes : ", str(safe_reports_nb)) # 514 OK
