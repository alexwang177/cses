import sys


def valid(arr, cap, k):

    if max(arr) > cap:
        return False

    groups = 1
    cur_sum = 0

    for x in arr:
        if cur_sum + x <= cap:
            cur_sum += x
        else:
            cur_sum = x
            groups += 1

    return groups <= k


n, k = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]

lo, hi = 0, sys.maxsize
ans = hi

while lo < hi:

    mid = lo + (hi - lo) // 2

    if valid(arr, mid, k):
        ans = mid
        hi = mid
    else:
        lo = mid + 1

print(lo)
