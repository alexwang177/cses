import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def mod_mul_inv(x, mod):
    return x**(mod-2) % mod


MOD = (10**9) + 7
n = int(sys.stdin.readline())
arr = list(range(1, n + 1))
total = sum(arr)

if total % 2 != 0:
    print(0)
    sys.exit()

target = total // 2

dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n):

    for s in range(1, target + 1):

        dp[i][s] = dp[i - 1][s]

        x = arr[i - 1]

        if s - x >= 0:
            dp[i][s] += dp[i - 1][s - x]
            dp[i][s] %= MOD

# for row in dp:
#     print(*row)

print(dp[n-1][target] % MOD)
