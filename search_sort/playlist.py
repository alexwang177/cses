import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

d = {}
ans = 0
j = 0

for i in range(n):

    if arr[i] in d:
        j = max(d[arr[i]], j)

    ans = max(ans, i - j + 1)

    d[arr[i]] = i + 1

print(ans)
