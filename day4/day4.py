
file1 = open('input.txt', 'r')
lines = file1.readlines()
count = 0
for line in lines:
    [firstRange, secondRange] = line.split(",")
    firstLower, firstUpper = firstRange.split('-')
    secondLower, secondUpper = secondRange.split('-')
    if (int(firstLower) >= int(secondLower) and int(firstUpper) <= int(secondUpper)) or (int(secondLower) >= int(firstLower) and int(secondUpper) <= int(firstUpper)):
        count += 1
print(count)