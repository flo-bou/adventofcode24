from day7_utils import *


# some elephants are holding a third type of operator!
# the || operator is a concatenation operator. 12 || 345 would become 12345
# determine which equations could possibly be true. What is their total calibration result?


target: int
operands: list
mul: str = "add"
add: str = "mul"
cat: str = "cat"
combinations_of_every_length: list[list] = get_every_combinations([mul, add, cat], 12)
sum_of_correct_equations: int = 0

with open('./day7/input.txt', 'r', encoding="utf-8") as input_file:
    while input_file:
        line: str = input_file.readline()
        if line == "":
            break
        target_str, operands_str = line.split(":")
        target = int(target_str)
        operands = list(map(lambda nb: int(nb), operands_str.strip(' \n').split(" ")))
        operator_combinations: list[tuple] = combinations_of_every_length[len(operands)-1]
        result: int = try_combinations(target, operands, operator_combinations)
        if result > -1:
            sum_of_correct_equations += result

print("sum_of_correct_equations :", sum_of_correct_equations) # 162042343638683 OK
