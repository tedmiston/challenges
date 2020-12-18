# load data
with open('input.txt') as fp:
    data = fp.read().strip().split()

# parse data
data = [int(x) for x in data]

# search for answer
match = False
first_number = None
second_number = None
for idx_i, i in enumerate(data):
    for idx_j, j in enumerate(data):
        if not match:
            if i + j == 2020:
                print('match:', i, j)
                match = True
                first_number = i
                second_number = j
                break

# print output
print(first_number * second_number)
