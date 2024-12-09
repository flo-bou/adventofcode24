import bisect


col1: list = list()
col2: list = list()
sum_of_distances = 0

# access the local file input.txt
with open('input.txt', 'r', encoding="utf-8") as input_file:
    while True:
        line = input_file.readline()
        if len(line) < 3:
            break
        # put the 2 column in 2 lists:
        nb1, nb2, *rest = line.strip(' \n').split('   ')
        # ordinate the 2 lists:
        bisect.insort(col1, int(nb1))
        bisect.insort(col2, int(nb2))

# for each pair, figure out the distance abs(a-b), then put it in an array (or directly accumulate)
# make the sum of every distance
for i in range(len(col1)):
    sum_of_distances += abs(col1[i]-col2[i])
    
print(sum_of_distances)
