import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    data.append(list(map(str, sys.stdin.readline().split())))

data = sorted(data, key = lambda x : int(x[0]))

for i in range(N):
    print(data[i][0], data[i][1])