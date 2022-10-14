import sys
from collections import deque

I, J = map(int, sys.stdin.readline().split())
data = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0
prev_result = 0

for _ in range(I):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(I):
    for j in range(J):
        if data[i][j] == 1:
            result += 1


def bfs():
    cnt = 0
    visited = [[False] * J for _ in range(I)]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (0 <= tx < I) and (0 <= ty < J) and visited[tx][ty] == 0:
                if data[tx][ty] == 0:
                    visited[tx][ty] = 1
                    queue.append([tx, ty])
                else:
                    data[tx][ty] = 0
                    visited[tx][ty] = 1
                    cnt += 1
    return cnt

time_cnt = 0
while result != 0:
    time_cnt += 1
    del_cheese = bfs()
    prev_result = result
    result -= del_cheese

print(time_cnt)
print(prev_result)