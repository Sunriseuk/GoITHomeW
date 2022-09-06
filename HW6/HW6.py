fh = open('F:\GoIT_Python_Project\GitHub\HomeWork\HW6\probe.txt', 'r')
sum = []
while True:
    line = fh.readline()
    if not line:
        break
    else:
        count = 0
        count2 = 0
        for i in line:
            if i != ',':
                count += 1
            else:
                break
        for j in line:
            if j != 'n':
                count2 += 1

        sum.append(line[count+1:count2])
fh.close()
# return sum
