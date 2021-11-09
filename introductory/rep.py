import sys

s = sys.stdin.readline()
ans = 0
cur = 0
prev = '#'

for c in s:
    if c != prev:
        ans = max(ans, cur)
        cur = 0

    cur += 1
    prev = c

print(ans)
