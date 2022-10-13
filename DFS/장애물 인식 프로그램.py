import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().strip())))

def dfs(i, j):
    if i < 0 or j < 0 or i > N-1 or j > N-1:
        return 0
    else:
        if data[i][j] == 1:
            data[i][j] = 0
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            return (up + down + left + right + 1)
        else:
            return 0

result = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            r = dfs(i, j)
            result.append(r)

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])
