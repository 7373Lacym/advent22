file1 = open('input.txt', 'r')
lines = file1.readlines()
for line in lines:
    cursor = 0
    while cursor < len(line) - 4:
        first = line[cursor]
        second = line[cursor + 1]
        third = line[cursor + 2]
        fourth = line[cursor + 3]
        test = set(first + second + third + fourth)
        cursor += 1
        if len(test) == 4:
            cursor += 3
            break;



print(cursor)