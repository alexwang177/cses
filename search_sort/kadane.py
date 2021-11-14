import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

max_sum = float("-inf")
cur_sum = 0

for x in arr:
    if x > cur_sum + x:
        cur_sum = x
    else:
        cur_sum += x

    max_sum = max(max_sum, cur_sum)

print(max_sum)
