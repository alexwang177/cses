import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

r = {}
cur_sum = 0
ans = 0

for x in arr:
    cur_sum += x

    if cur_sum % n == 0:
        ans += 1

    if cur_sum % n in r:
        ans += r[cur_sum % n]
        r[cur_sum % n] += 1
    else:
        r[cur_sum % n] = 1

print(ans)
