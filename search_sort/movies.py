import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    p = tuple(int(x) for x in sys.stdin.readline().strip().split(" "))
    arr.append(p)

arr.sort(key=lambda x: x[1])

ans = 0
cur_end = 0

for x in arr:
    if x[0] >= cur_end:
        cur_end = x[1]
        ans += 1

print(ans)
