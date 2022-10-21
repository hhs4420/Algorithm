# 22:15
import sys
import heapq

N = int(sys.stdin.readline())

result = []

for _ in range(N):
    s, f = map(int, sys.stdin.readline().split())
    heapq.heappush(result, (f, s))

prev_f = 0
count = 0

while result:
    f, s = heapq.heappop(result)
    if count == 0:
        count += 1
        prev_f = f
    
    elif s >= prev_f:
        count += 1
        prev_f = f

print(count)

