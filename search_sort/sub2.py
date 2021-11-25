import sys

n, target = [int(x) for x in sys.stdin.readline().split(" ")]
arr = [int(x) for x in sys.stdin.readline().split(" ")]
sum_map = {}

cur_sum = 0
ans = 0

for i in range(n):

    cur_sum += arr[i]

    if cur_sum == target:
        ans += 1

    # cur_sum - x = target
    x = cur_sum - target

    if x in sum_map:
        ans += sum_map[x]

    if cur_sum in sum_map:
        sum_map[cur_sum] += 1
    else:
        sum_map[cur_sum] = 1

print(ans)
