file1 = open('input.txt', 'r')
lines = file1.readlines()
for line in lines:
    cursor = 0
    while cursor < len(line) - 14:

        sub = list(line[cursor:(cursor+14)])
        target = set(sub)
        cursor += 1
        if len(target) == 14:
            cursor += 13
            break;

print(cursor)