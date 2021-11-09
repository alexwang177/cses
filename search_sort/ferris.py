import sys

'''

4 10
7 2 3 9

2 3 7 9

'''

n, x = [int(x) for x in sys.stdin.readline().strip().split(" ")]
arr = [int(x) for x in sys.stdin.readline().strip().split(" ")]

arr.sort()

lo = 0
hi = n - 1
ans = 0

while lo <= hi:

    if lo == hi:
        ans += 1
        break
    elif arr[lo] + arr[hi] <= x:
        lo += 1
        hi -= 1
    else:
        hi -= 1

    ans += 1

print(ans)
