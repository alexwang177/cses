import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, target = ria()
coins = ria()
coins.sort()
MAX = 1000000007

dp = [MAX for _ in range(target + 1)]
dp[0] = 0

for i in range(coins[0], target + 1):

    best = MAX

    for c in coins:

        if i - c >= 0:
            best = min(best, dp[i - c])
        else:
            break

    dp[i] = best + 1

# print(dp)

print(-1 if dp[target] >= MAX else dp[target])
