# 01:57

import sys

N = int(sys.stdin.readline())

data = []

for _ in range(N):
    s = sys.stdin.readline()
    data.append(s)

result = 0

for s in data:
    tmp = []
    last_tmp = ''
    corr = 1
    for ss in s:
        if ss in tmp and ss != last_tmp:
            corr = 0
            break
        else:
            tmp.append(ss)
            last_tmp = ss
    if corr == 1:
        result += 1

print(result)