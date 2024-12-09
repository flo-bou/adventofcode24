import re

# input is a corrupted memory of computer
# goal of the program is to multiply some numbers 
# in the form of mul(X,Y) where x ans y are 1-3 digits
# many characters are invalid and should be ignored
# search for the good sequences then execute the multiplication then add them all up


#rechecher les séquences exactes mul(x,y) où x et y sont composés de 1 à 3 chiffres
pattern = re.compile('mul\([\d]{1,3},[\d]{1,3}\)')
sequences = []
sum = 0
# data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def mul(a, b):
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
    sum += eval(seq) # safiser ?

print(sum) # 168539636
