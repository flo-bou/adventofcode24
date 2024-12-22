import re

# 2 new instructions need to be handle
# After the 'do()' instruction, you must the mul(x,y) instructions until the 'don't()' re-appears
# After the 'don't()' instruction, you must not execute the mul(x,y) instructions until the 'do()' re-appears
# sum up all the results of mul()


# découper le string: trouver les séquences/string entre 'do()' et 'don't()'
# + le premier string avant do ou dont + le dernier string après do sans dont
# pour chaque string, refaire la recherche précédente

# get_start: re.Pattern = re.compile("do\(\).*don't\(\)")
# get_end: re.Pattern = re.compile("do\(\).*don't\(\)")
# Découpage principale jsute avec split() ?
get_between_do_and_dont: re.Pattern = re.compile("do\(\).*don't\(\)")


# rechecher les séquences exactes mul(x,y) où x et y sont composés de 1 à 3 chiffres
get_mul: re.Pattern = re.compile('mul\([\d]{1,3},[\d]{1,3}\)')
good_chunks: list = []
mul_sequences: list = []
sum: int = 0


def mul(a: int, b: int) -> int:
    return a*b


with open('./day3/input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line = input_file.readline()
        if len(line) == 0:
            break
        # mettre les sequences dans une liste
        good_chunks.extend(re.findall(get_between_do_and_dont, line))
        # re.search plutot que findall() ?


for seq in mul_sequences:
    print(seq)
# reduce la liste en accumulant les résultats
# for seq in sequences:
#     sum += eval(seq) # à safiser ?

print(sum) # 168539636
