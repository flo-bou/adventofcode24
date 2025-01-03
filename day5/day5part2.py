# find updates in incorrect order
# fix them up following the rules
# add the middle number of theses corrected updates up


rules: list[list] = list()
updates: list[list] = list()
incorrect_updates: list = list()
final_sum = 0


with open('./day5/input.txt', 'r', encoding="utf-8") as input_file:
    # récupérer toutes les paires de rules :
    while True:
        line: str = input_file.readline()
        if line == "\n":
            break
        rules.append(list(map(lambda x: int(x), line.strip(' \n').split("|"))))
    # récuperer toutes les updates :
    while True:
        line: str = input_file.readline()
        if len(line) == 0:
            break
        updates.append(list(map(lambda x: int(x), line.strip(' \n').split(","))))


# Lire chaque update et 
# lire chaque nombre de l'update et pour chacun, vérifier toutes les règles (ou plutot trouver les règles enfreintes)

for update in updates:
    for page_index, page in enumerate(update):
        # trouver toutes les règles qui commencent par page
        for rule in rules:
            if page == rule[0]:
                # trouver celles dont le 2e nombre est bien présent dans update[i] :
                if rule[1] in update: 
                    # parmi celles-ci trouver les cas fautifs, cad si ce 2e nombre est avant le 1er
                    if page_index > update.index(rule[1]):
                        incorrect_updates.append(update)

# VERIFIER
# corriger l'update : trouver le second membre, le retirer puis le réinsérer juste après le premier. Puis relancer le test sur la série/update
for update in incorrect_updates:
    for page_index, page in enumerate(update):
        for rule in rules:
            if page == rule[0]:
                # trouver celles dont le 2e nombre est bien présent dans update[i] :
                if rule[1] in update: 
                    update.remove(rule[1])
                    update.insert(update.index(rule[0])+1, rule[1])
                    # puis relancer la détection sur cette update


print(len(incorrect_updates), "updates incorrects ont été trouvés sur les", len(updates))

for update in incorrect_updates:
    middle_index = int(len(update)/2)
    final_sum += update[middle_index]

print("La somme des membres centraux des updates incorrects corrigés est", final_sum) # 279955 FALSE !!
