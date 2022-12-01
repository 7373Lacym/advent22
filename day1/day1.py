file1 = open('input.txt', 'r')
Lines = file1.readlines()
  
count = 0
res = [0] * len(Lines)
curMax = 0
for line in Lines:
    if line == '\n':
        count += 1

    else:
        intLine = int(line)
        res[count] = (intLine + res[count])
        curMax = max(curMax, res[count])

res.sort()
res.reverse()
print(res[0] + res[1] + res[2])
