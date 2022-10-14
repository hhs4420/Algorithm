import sys

N = int(sys.stdin.readline())

result_dict = {1 : 1, 2 : 0, 3 :0}

for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    x_data = result_dict[X]
    y_data = result_dict[Y]

    result_dict[X] = y_data
    result_dict[Y] = x_data

for i in range(1, 4):
    if result_dict[i] == 1:
        print(i)