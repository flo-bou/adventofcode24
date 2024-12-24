import re

# input is a corrupted memory of computer
# goal of the program is to multiply some numbers 
# in the form of mul(X,Y) where x and y are 1-3 digits
# many characters are invalid and should be ignored
# search for the good sequences then execute the multiplication then add them all up


# rechecher les séquences exactes mul(x,y) où x et y sont composés de 1 à 3 chiffres
pattern: re.Pattern = re.compile('mul\([\d]{1,3},[\d]{1,3}\)')
sequences: list = []
sum: int = 0


def mul(a: int, b: int):
    return a*b


with open('./day3/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line = input_file.readline()
        if len(line) == 0:
            break
        # mettre les sequences dans une liste
        sequences.extend(re.findall(pattern, line))


print(sequences)
# reduce la liste en accumulant les résultats
for seq in sequences:
    sum += eval(seq) # à safiser ?

print(sum) # 168539636 OK
