file1 = open('input.txt', 'r')
lines = file1.readlines()
count = 0
#     [C]         [Q]         [V]
#     [D]         [D] [S]     [M] [Z]
#     [G]     [P] [W] [M]     [C] [G]
#     [F]     [Z] [C] [D] [P] [S] [W]
# [P] [L]     [C] [V] [W] [W] [H] [L]
# [G] [B] [V] [R] [L] [N] [G] [P] [F]
# [R] [T] [S] [S] [S] [T] [D] [L] [P]
# [N] [J] [M] [L] [P] [C] [H] [Z] [R]
#  1   2   3   4   5   6   7   8   9

#     [D]
# [N] [C]
# [Z] [M] [P]
one = ['N', 'Z']
two = ['D', 'C', 'M']
three = ['P']

collect = [one, two, three]
for line in lines:
    quantity, source, destination = line.split(" ")
    quantity = int(quantity)
    source = int(source)
    destination = int(destination)
    while quantity > 0:
        temp = collect[source - 1].pop(0)
        collect[destination - 1].insert(0, temp)
        quantity -= 1

res = ""
for item in collect:
    res += item.pop(0)

print(res)