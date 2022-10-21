# 02:44

import sys

N = int(sys.stdin.readline())

data = []

for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N - i - 1):
        data[i].append(-1)

dp = []

for i in range(N):
    dp.append([])
    for j in range(N):
        dp[i].append(0)


dp[0][0] = data[0][0]

for i in range(1, N):
    for j in range(N):
        if data[i][j] != -1:

            if j == 0:
                dp[i][j] = data[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = data[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = data[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[N-1]))