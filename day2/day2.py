# rock -> 1
# paper = 2
#scicor = 3
#win 6
#draw 3
#lose 0
# A -> rock
# B -> paper
# C -> scicors
# X -> rock
# Y -> paper
# Z -> scicors

# A X -> 1 + 3 = 4
# A Y -> 2 + 6 = 8
# A Z -> 3 + 0 = 3

# B X -> 1 + 0 = 1
# B Y -> 2 + 3 = 5
# B Z -> 3 + 6 = 9

# C X -> 1 + 6 = 7
# C Y -> 2 + 0 = 2
# C Z -> 3 + 3 = 6


lookup = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
res = [0] * len(Lines)
curMax = 0
sum = 0
for line in Lines:
    sum += lookup[(line.strip())]

print(sum)