
# puzzle input is a word search
# you must search the word "XMAS" in the input file
# the word can be writter in horizontal, vertical, diagonal (2 diagonals) and for all of these direction, they can be written backward. 
# The same letter can be used with differents findings



data: list = list()
detection: int = 0
# line_index: int = 0

def detect_XMAS(data: list, line_nb: int, char_index: int):
    result = 0
    # faire les détections dans les 8 directions
    # direction Est :
    if (
        len(data[line_nb]) >= char_index+4 and
        data[line_nb][char_index] + 
        data[line_nb][char_index+1] +
        data[line_nb][char_index+2] + 
        data[line_nb][char_index+3] == "XMAS"
    ):
        print("XMAS détecté dans la direction Est à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    # direction Sud-Est :
    if (
        len(data) >= line_nb+4 and
        len(data[line_nb]) >= char_index+4 and
        data[line_nb][char_index] + 
        data[line_nb+1][char_index+1] + 
        data[line_nb+2][char_index+2] + 
        data[line_nb+3][char_index+3] == "XMAS"
    ):
        print("XMAS détecté dans la direction Sud-Est à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    # direction Sud :
    if (
        len(data) >= line_nb+4 and
        data[line_nb][char_index] + 
        data[line_nb+1][char_index] +
        data[line_nb+2][char_index] + 
        data[line_nb+3][char_index] == "XMAS"
    ):
        print("XMAS détecté dans la direction Sud à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    # direction Sud-Ouest :
    if (
        len(data) >= line_nb+4 and
        char_index-3 >= 0 and
        data[line_nb][char_index] + 
        data[line_nb+1][char_index-1] + 
        data[line_nb+2][char_index-2] + 
        data[line_nb+3][char_index-3] == "XMAS"
    ):
        print("XMAS détecté dans la direction Sud-Ouest à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    # direction Ouest :
    if (
        char_index-3 >= 0 and
        data[line_nb][char_index] + 
        data[line_nb][char_index-1] +
        data[line_nb][char_index-2] + 
        data[line_nb][char_index-3] == "XMAS"
    ):
        print("XMAS détecté dans la direction Ouest à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    # direction Nord-Ouest :
    if (
        line_nb-3 >= 0 and
        char_index-3 >= 0 and
        data[line_nb][char_index] + 
        data[line_nb-1][char_index-1] + 
        data[line_nb-2][char_index-2] + 
        data[line_nb-3][char_index-3] == "XMAS"
    ):
        print("XMAS détecté dans la direction Nord-Ouest à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    # direction Nord :
    if (
        line_nb-3 >= 0 and
        data[line_nb][char_index] + 
        data[line_nb-1][char_index] +
        data[line_nb-2][char_index] + 
        data[line_nb-3][char_index] == "XMAS"
    ):
        print("XMAS détecté dans la direction Nord à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    # direction Nord-Est :
    if (
        line_nb-3 >= 0 and
        len(data[line_nb]) >= char_index+4 and
        data[line_nb][char_index] + 
        data[line_nb-1][char_index+1] + 
        data[line_nb-2][char_index+2] + 
        data[line_nb-3][char_index+3] == "XMAS"
    ):
        print("XMAS détecté dans la direction Nord-Est à la ligne", line_nb, "et à l'index", char_index)
        result += 1
    return result


# put the data in a variable :
with open('./day4/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line: str = input_file.readline()
        if len(line) == 0:
            break
        data.append(line.strip('\n'))

# lire dans l'ordre tout le contenu et à chaque lettre 'X', lancer une fonction de détection dans chaque sens (faire tous les sens même si 1 sens a déjà donné une détection fructueuse)
for line_nb, line in enumerate(data):
    for char_index, char in enumerate(line):
        if char == 'X':
            detection += detect_XMAS(data, line_nb, char_index)

print(detection, "détections") # 2524 OK
