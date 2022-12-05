import math

file1 = open('input.txt', 'r')
lines = file1.readlines()

def getPri(letter):
    if letter.isupper():
        return ord(letter) - 38
    return ord(letter) - 96


total = 0
counter = 0
lineOne = ""
lineTwo = ""
for line in lines:
    if counter == 0:
        lineOne = line
        counter += 1
    elif counter == 1:
        lineTwo = line
        counter += 1
    elif counter == 2:
        for item in lineOne:
            if item in lineTwo and item in line:
                total += getPri(item)
                counter = 0
                break
        counter = 0
        lineOne = ""
        lineTwo = ""

print(total)