import sys

n, target = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]

lo, hi = 1, int(sys.maxsize)

while lo < hi:
    mid = lo + (hi - lo) // 2

    product = 0
    for time in arr:
        product += mid // time

    if product >= target:
        hi = mid
    else:
        lo = mid + 1

print(lo)
