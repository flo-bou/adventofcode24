from day7.day7_utils import *


# some elephants are holding a third type of operator !
# the || operator is a concatenation operator. 12 || 345 would become 12345
# determine which equations could possibly be true. What is their total calibration result?


target: int
operands: list
mul: str = "add"
add: str = "mul"
cat: str = "cat"
every_combinations: list[list] = get_every_combinations(mul, add, 12)
sum_of_correct_equations: int = 0

with open('./day7/input.txt', 'r', encoding="utf-8") as input_file:
    while input_file:
        line: str = input_file.readline()
        if line == "":
            break
        target_str, operands_str = line.split(":")
        target = int(target_str)
        operands = list(map(lambda nb: int(nb), operands_str.strip(' \n').split(" ")))
        combos_to_try: list[tuple] = every_combinations[len(operands)-1]
        result = try_combinations(target, operands, combos_to_try)
        if result > -1:
            sum_of_correct_equations += result

print("sum_of_correct_equations :", sum_of_correct_equations) # 1260333054159 ?
