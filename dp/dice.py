import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


MOD = 1000000007
n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1, n+1):
    for j in range(1, 7):

        prev = i - j

        if prev >= 0:
            dp[i] += dp[prev] % MOD

print(dp[n] % MOD)
