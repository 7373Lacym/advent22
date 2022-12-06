file1 = open('input.txt', 'r')
lines = file1.readlines()
count = 0

def isCompleteOverlap(firstLower, firstUpper, secondLower, secondUpper):
    return (int(firstLower) >= int(secondLower) and int(firstUpper) <= int(secondUpper)) or (
            int(secondLower) >= int(firstLower) and int(secondUpper) <= int(firstUpper))


def isPartialOverlap(firstLower, firstUpper, secondLower, secondUpper):
    return int(secondLower) <= int(firstUpper) <= int(secondUpper) or int(firstLower) <= int(secondUpper) <= int(firstUpper)


for line in lines:
    [firstRange, secondRange] = line.split(",")
    firstLower, firstUpper = firstRange.split('-')
    secondLower, secondUpper = secondRange.split('-')
    if isCompleteOverlap(firstLower, firstUpper, secondLower, secondUpper) or isPartialOverlap(firstLower, firstUpper, secondLower, secondUpper):
        count += 1
print(count)



