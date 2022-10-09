import sys

N = int(sys.stdin.readline())

data = list(map(str, sys.stdin.readline().split()))

i = 1
j = 1

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for s in data:
    ti = 0
    tj = 0
    # 이동 후 좌표 구하기
    for m in range(len(move_types)):
        if s == move_types[m]:
            ti = i + di[m]
            tj = j + dj[m]
    if ti < 1 or tj < 1 or ti > N or tj > N:
        continue
    else:
        i, j = ti, tj


print(i, j)

