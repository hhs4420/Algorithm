import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = []
visited = [False] * (N + 1)
result = 0

for _ in range(N + 1):
    graph.append([])

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

for i in range(1, N + 1):
    if visited[i] == False:
        dfs(i)
        result += 1

print(result)