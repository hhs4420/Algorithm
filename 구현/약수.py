import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

result = 0

if N == 1:
    result = data[0] ** 2

else:
    data = sorted(data)
    M = len(data)
    result = data[0] * data[M-1]

print(result)