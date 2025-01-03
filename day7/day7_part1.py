from day7.day7_utils import *

# operators has been stolen by young elephants !
# need to determine which test values could possibly be produced by placing any combination of operators into the calibration equations (the input)
# each line is an equation. You need to determine whether the number can be combined with operators (only one or several per equation ?) to get the value on the left side
# operators are always evaluated left to rigth, ignoring mathematical precedence rules. numbers must not be rearranged
# The operators are + and *
# detect the correct equations (the one that can be resolved with operators)
# then add all the results up

# read the file 
# for each line, process the calculation
# test all the possibilities of operators agains the result

target: int
operands: list
mul: str = "add"
add: str = "mul"
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

print("sum_of_correct_equations :", sum_of_correct_equations) # 1260333054159 OK
