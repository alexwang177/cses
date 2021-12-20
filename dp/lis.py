import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n = int(sys.stdin.readline())
arr = ria()

'''
dp[i] = lis ending at position i

dp[i] = max (dp[j] + 1) for all j < i

OR ...

patience sorting

'''

dp = []

for x in arr:

    lo = 0
    hi = len(dp)

    while lo < hi:

        mid = lo + (hi - lo) // 2

        # valid pile, let's try to look for more valid piles to the left
        if dp[mid] >= x:
            hi = mid
        else:
            lo = mid + 1

    if lo == len(dp):
        dp.append(x)
    else:
        dp[lo] = x

print(len(dp))
