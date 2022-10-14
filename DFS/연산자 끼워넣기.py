import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))

maximum = -1000000000
minimum = 1000000000

def dfs(count, val, b):
    global maximum, minimum
    if count == N - 1:
        maximum = max(val, maximum)
        minimum = min(val, minimum)

    else:
        if b[0] != 0:
            dfs(count + 1, val + A[count + 1], [b[0] - 1, b[1], b[2], b[3]])
        if b[1] != 0:
            dfs(count + 1, val - A[count + 1], [b[0], b[1] - 1, b[2], b[3]])
        if b[2] != 0:
            dfs(count + 1, val * A[count + 1], [b[0], b[1], b[2] - 1, b[3]])
        if b[3] != 0:
            dfs(count + 1, int(val / A[count + 1]), [b[0], b[1], b[2], b[3] - 1])

dfs(0, A[0], B)

print(maximum)
print(minimum)
