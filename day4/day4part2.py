# the detection should be 2 "MAS" sequences in cross (diagonally) in any direction
# letters (exept "A") can be in multiples detections


def detect_MAS(data: list, line_index: int, col_index: int) -> bool:
    result: bool = False
    # N-O <-> S-E
    detect1: str = data[line_index-1][col_index-1] + 'A' + data[line_index+1][col_index+1]
    # S-O <-> N-E
    detect2: str = data[line_index+1][col_index-1] + 'A' + data[line_index-1][col_index+1]
    if (detect1 == "MAS" or detect1 == "SAM") and (detect2 == "MAS" or detect2 == "SAM"):
        result = True
    return result

def main():
    data: list[str] = list()
    detection_nb: int = 0
    with open('./day4/input.txt', 'r', encoding="utf-8") as input_file:
        while True:
            line: str = input_file.readline()
            if len(line) == 0:
                break
            data.append(line.strip('\n'))

    # lire dans l'ordre tout le contenu et à chaque lettre 'A', lancer la fonction de détection
    for line_index, line in enumerate(data):
        if line_index == 0 or line_index == len(data)-1:
            continue
        for col_index, char in enumerate(line):
            if char == 'A' and (col_index != 0 and col_index != len(line)-1):
                if detect_MAS(data, line_index, col_index):
                    detection_nb += 1

    print(detection_nb, "détections") # 1873 OK


if __name__ == "__main__":
    main()
