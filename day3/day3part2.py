import re

# 2 new instructions need to be handle
# After the 'do()' instruction, you must execute the mul(x,y) instructions until the 'don't()' re-appears
# After the 'don't()' instruction, you must not execute the mul(x,y) instructions until the 'do()' re-appears
# sum up all the results of mul()


# découper le string: trouver les séquences/string entre 'do()' et 'don't()'
# + le premier string avant do ou dont + le dernier string après do sans dont
# pour chaque string, refaire la recherche précédente


do_pattern: re.Pattern = re.compile('do\(\)')
dont_pattern: re.Pattern = re.compile("don't\(\)")
mul_pattern: re.Pattern = re.compile('mul\([\d]{1,3},[\d]{1,3}\)')
start: int
length: int
allowed_chunks: list[str] = []
mul_sequences: list[str] = []
sum: int = 0


def mul(a: int, b: int) -> int:
    return a*b

data = ""
with open('./day3/input.txt', 'r', encoding="utf-8") as input_file:
    datas: list[str] = input_file.readlines()
for line in datas:
    data += (line.strip(" \n"))
# print(len(data))

# search() permet de trouver la 1ere occurence

first_do_match: re.Match = re.match("", "")

while first_do_match:
    # récupérer le str raccourci du début avant 'do()'
    first_do_match = re.search(do_pattern, data)
    if first_do_match:
        start = first_do_match.start()
        first_dont_match = re.search(dont_pattern, data[start:])
        if first_dont_match:
            length = first_dont_match.end()
            allowed_chunks.append(data[start:start+length])
            data = data[start+length:]
        else:
            allowed_chunks.append(data[start:])
            break
    else:
        break


for chunk in allowed_chunks:
    mul_sequences.extend(re.findall(mul_pattern, chunk))

for seq in mul_sequences:
    sum += eval(seq) # à safiser ?

# le début avant le 1er do() ou dont() compte ?
print(sum) # 95297817
