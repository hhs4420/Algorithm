import sys
from collections import deque

N, M, I = map(int, sys.stdin.readline().split())

graph = []

visited = [False] * (N + 1)

dfs_result = []

bfs_result = []

for _ in range(N + 1):
    graph.append([])

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def dfs(v):
    if visited[v] == False:
        visited[v] = True
        dfs_result.append(v)
        for i in graph[v]:
            if visited[i] == False:
                dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        bfs_result.append(x)
        for i in graph[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(I)

visited = [False] * (N + 1)
bfs(I)


count = 0
for i in dfs_result:
    count += 1
    if count != N:
        print(i, end = ' ')
    else:
        print(i)
        count = 0


for i in bfs_result:
    count += 1
    if count != N:
        print(i, end = ' ')
    else:
        print(i)
        count = 0