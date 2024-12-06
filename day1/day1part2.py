
col_1 = set()
col_2 = list()
similarity_score = 0;

with open('input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line = input_file.readline()
        if len(line) < 3:
            break
        nb1, nb2, *rest = line.strip(' \n').split('   ')
        col_1.add(int(nb1))
        col_2.append(int(nb2))

for val in col_1:
    # similarity score = somme de (tous les nombre de gauche multipliés par le nombre de fois qu'ils apparaissent à droite)
    similarity_score += col_2.count(val) * val

print("Similarity score : " + str(similarity_score))
