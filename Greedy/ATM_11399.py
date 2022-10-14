import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

data_dict = {}

for i in range(1, N + 1):
    data_dict[i] = data[i - 1]

data_dict = sorted(data_dict.items(), key = lambda x: x[1])

data_sum = 0
result = 0

for i in data_dict:
    data_sum += i[1]
    result += data_sum

print(result)
