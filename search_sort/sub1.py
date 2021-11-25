import sys

n, x = [int(x) for x in sys.stdin.readline().split(" ")]
arr = [int(x) for x in sys.stdin.readline().split(" ")]

cur_sum = 0
j = 0
ans = 0

for i in range(n):
    cur_sum += arr[i]

    while j < i and cur_sum > x:
        cur_sum -= arr[j]
        j += 1

    if cur_sum == x:
        ans += 1

print(ans)
