import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

result_y = 0
result_m = 0

# 영식
for i in data:
    n = int(i / 30)
    result_y += (n + 1) * 10

# 민식
for i in data:
    n = int(i / 60)
    result_m += (n + 1) * 15

if result_y < result_m:
    print("Y", result_y)
elif result_y > result_m:
    print("M", result_m)
else:
    print("Y", "M", result_y)