import sys

data = []
asum = 0
for i in range(9):
    n = int(sys.stdin.readline())
    data.append(n)
    asum += n

data.sort()

for i in range(9):
    for j in range(i+1, 9):
        if i == j:
            continue
        else:
            if asum - data[i] - data[j] == 100:
                data1 = data[i]
                data2 = data[j]
                data.remove(data1)
                data.remove(data2)
                for k in range(7):
                    print(data[k])
                exit()