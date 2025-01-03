import re

# 2 new instructions need to be handle
# After the 'do()' instruction, you must execute the mul(x,y) instructions until the 'don't()' re-appears
# After the 'don't()' instruction, you must not execute the mul(x,y) instructions until the 'do()' re-appears
# sum up all the results of mul()
# At the beginning of the program, mul instructions are enabled.

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
sum_of_instructions: int = 0


def mul(a: int, b: int) -> int:
    return a*b

data: str = "" # big str containing the imput
with open('./day3/input.txt', 'r', encoding="utf-8") as input_file:
    lines: list[str] = input_file.readlines()

for line in lines:
    data += (line.strip("\n"))

# fonction qui récupère une string et renvoie la 1ere substring entre do et dont (ou fin) ainsi que le reste de la string après don't(). Si data est vide, on est arrivé au bout de la chaine.
def get_do_substr(data: str) -> list[str]:
    """Lit une chaine de caractères et renvoie la 1ere sous-chaine entre "do()" et "don't()" ainsi que la chaine initiale raccourci à partir de la fin de la chaine trouvée.

    Args:
        data (str): Chaine dans laquelle chercher

    Returns:
        tuple[str]: La 1ere sous-chaine trouvé (chaine vide si rien n'a été trouvé), et data raccourci jusqu'à la fin de la chaine trouvée (chaine vide si on est arrivé à la fin de data).
    """
    allowed_chunk: str
    data_out: str
    do_pattern: re.Pattern = re.compile('do\(\)')
    dont_pattern: re.Pattern = re.compile("don't\(\)")
    
    first_do_match: re.Match = re.search(do_pattern, data)
    if not first_do_match:
        # s'il n'y a plus de do(), alors il n'y a pas de substring correct et on peut renvoyer une chaine vide pour data_out
        allowed_chunk = ""
        data_out =""
    else:
        first_do_index: int = first_do_match.start()
        # redécoupage au cas où il y ait plusieurs dont() de suite :
        data = data[first_do_index:]
        
        first_dont_match: re.Match = re.search(dont_pattern, data)
        if not first_dont_match:
            # s'il n'y a plus de don't(), alors le reste de data est correct et renvoyé, data_out est vide
            allowed_chunk = data
            data_out = ""
        else:
            first_dont_index: int = first_dont_match.start()
            allowed_chunk = data[:first_dont_index]
            data_out = data[first_dont_index:]
    return allowed_chunk, data_out


# faire un découpage initial pour récupérer les "mul()" avant le 1er "don't()"
first_dont_match = re.search(dont_pattern, data)
start: int = first_dont_match.start()
allowed_chunks.append(data[:start])
data = data[start:]

while len(data) > 0:
    allowed_chunk, data = get_do_substr(data)
    allowed_chunks.append(allowed_chunk)

for chunk in allowed_chunks:
    mul_sequences.extend(re.findall(mul_pattern, chunk))
print("mul sequences :", mul_sequences)

for seq in mul_sequences:
    sum_of_instructions += eval(seq)

print(sum_of_instructions) # 97529391 OK
