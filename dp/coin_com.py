import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, target = ria()
coins = ria()
coins.sort()
MOD = (10**9)+7

dp = [0]*(target+1)
dp[0] = 1

for i in range(target + 1):

    for c in coins:
        if i + c > target:
            break
        else:
            dp[i+c] = (dp[i+c] + dp[i]) % MOD

print(dp[target] % MOD)
