import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


'''

n = 2
ans = 8

'''

t = int(sys.stdin.readline())
MOD = (10**9)+7

dp = [[0 for _ in range(1000001)] for _ in range(2)]

'''
dp[0][i] = number of possible towers of height i such that the 2x1 block at height i is united
dp[1][i] = number of possible towers of height i such that the 2x1 block at height i is not united
'''

dp[0][1] = 1
dp[1][1] = 1

for i in range(2, 1000001):

    dp[0][i] += 2 * dp[0][i-1]
    dp[0][i] += dp[1][i-1]
    dp[1][i] += dp[0][i-1]
    dp[1][i] += 4 * dp[1][i-1]

    dp[0][i] %= MOD
    dp[1][i] %= MOD

for _ in range(t):

    n = int(sys.stdin.readline())
    ans = (dp[0][n] + dp[1][n]) % MOD

    print(ans)
