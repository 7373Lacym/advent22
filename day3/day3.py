import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

def getPri(letter):
    if letter.isupper():
        return ord(letter) - 38
    return ord(letter) - 96

sum = 0
for line in lines:
    middleIndice = math.floor(len(line)/2)
    firstHalf = line[0:middleIndice]
    secondHalf = line[middleIndice:len(line)]
    for item in firstHalf:
        if item in secondHalf:
            sum += getPri(item)
            break;

print(sum)