from day11_utils import *

# each stone has a number
# every time you blink, the stones change with a consistent behavior
# then all change simultaneously according to the first appliable rule in this list :
# 0 becomes 1
# if even number of digits, it is replaced by 2 stones with the half each. leading 0 are removed. Exemple : 1201 becomes 12 1
# else (odd number of digits exept for "0") the number is multiplied by 2024

# the stones keep their order
# how many stones will you have after 25 blinks ?


def main():
    stones: list = list()

    with open('./day11/input.txt', 'r', encoding="utf-8") as input_file:
        while input_file:
            line: str = input_file.readline()
            if line == "":
                break
            stones.extend(list(map(lambda x: int(x), line.strip(' \n').split(" "))))
            print(stones)


    print("Au départ, il y a", len(stones), "pierres")
    for i in range(25):
        stones = blink(stones)
        print("Après", i+1, "itérations, il y a", len(stones), "pierres") # 198089 OK


if __name__ == "__main__":
    main()
