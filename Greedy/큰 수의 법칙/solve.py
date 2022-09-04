N, M, K = map(int, input().split())
data = list(map(int, input().split()))

largest = 0
large_i = 0

for i in range(0, N):
    if data[i] > largest:
        largest = data[i]
        large_i = i

second = 0

for i in range(0, N):
    if i == large_i:
        pass
    elif data[i] > second:
        second = data[i]

count = 0
answer = 0

for i in range(0, M):
    if count == K:
        answer += second
        count = 0
    else:
        answer += largest
        count += 1

print(answer)