import sys

T = int(sys.stdin.readline())

N = []
M = []

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    N.append(n)
    M.append(m)

def factorial(v):
    if v <= 1:
        return 1
    else:
        return v * factorial(v-1)

for i in range(T):
    print(int(factorial(M[i]) / (factorial(N[i]) * factorial(M[i] - N[i]))))
