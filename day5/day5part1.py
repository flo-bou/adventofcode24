
# new pages must be printed in a specific order
# X|Y means if X and Y must be produced in an update, X must be printed at one point before Y
# there are 2 inputs : the page ordering rules in form of X|Y pairs and the page to produce in each update
# we dont know if the updates respect the ordering rules
# identify which updates respect the ordering rules
# then find the middle page number of each correctly-ordered update
# then add them all up 

rules: list = list()
updates: list = list()
correct_updates: list = list()
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
    is_update_correct = True
    for page_index, page in enumerate(update):
        # trouver toutes les règles qui commencent par page
        is_page_correct = True
        for rule in rules:
            if page == rule[0]:
                # trouver celles dont le 2e nombre est bien présent dans update[i] :
                if rule[1] in update: 
                    # parmi celles-ci trouver les cas fautifs, cad si ce 2e nombre est avant le 1er
                    if page_index > update.index(rule[1]):
                        is_page_correct = False
                        print("La règle", rule, "a été enfreinte dans l'update", update)
                        break
        if not is_page_correct:
            is_update_correct = False
            break
    if is_update_correct:
        # remplir une nouvelle liste contenant les updates corrects
        correct_updates.append(update)

print(len(correct_updates), "updates corrects ont été trouvés sur les", len(updates))

for update in correct_updates:
    middle_index = int(len(update)/2)
    final_sum += update[middle_index]

print("La somme des membres centraux des updates corrects est", final_sum) # 5639 OK
