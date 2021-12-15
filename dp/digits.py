import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n = int(sys.stdin.readline())

# dp[x] is the min number of moves to make x

dp = {n: 0}

for x in range(n, -1, -1):

    if x in dp:

        for d in str(x):
            d = int(d)
            nxt = x - d
            dp[nxt] = min(dp[nxt] if nxt in dp else float("inf"), dp[x] + 1)

print(dp[0])
