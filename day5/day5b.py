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

one = ['P', 'G',  'R',  'N']
two = ['C', 'D', 'G', 'F', 'L', 'B', 'T', 'J']
three = ['V', 'S', 'M']
four = ['P', 'Z', 'C', 'R', 'S', 'L']
five = ['Q', 'D', 'W', 'C', 'V', 'L', 'S', 'P']
six = ['S', 'M', 'D', 'W', 'N', 'T', 'C']
seven = ['P', 'W', 'G', 'D', 'H']
eight = ['V', 'M', 'C', 'S', 'H', 'P', 'L', 'Z']
nine = ['Z', 'G', 'W', 'L', 'F', 'P', 'R']

collect = [one, two, three, four, five, six, seven, eight, nine]

# one = ['N', 'Z']
# two = ['D', 'C', 'M']
# three = ['P']
#
# collect = [one, two, three]
for line in lines:
    quantity, source, destination = line.split(" ")
    quantity = int(quantity)
    source = int(source)
    destination = int(destination)
    thingToKeepOrder = []
    while quantity > 0:
        temp = collect[source - 1].pop(0)
        thingToKeepOrder.insert(0, temp)
        quantity -= 1
    for item in thingToKeepOrder:
        collect[destination - 1].insert(0, item)

res = ""
for item in collect:
    res += item.pop(0)

print(res)