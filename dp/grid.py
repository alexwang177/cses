import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def rca():
    return list(sys.stdin.readline().strip())


MOD = (10**9)+7
n = int(sys.stdin.readline())
grid = []

for _ in range(n):
    grid.append(rca())

# print(grid)

if grid[0][0] == '*':
    print(0)
    sys.exit()

dp = [[0 for _ in range(n)] for _ in range(n)]

# dp[i][j] is number of ways to reach position i,j

dp[0][0] = 1

for i in range(n):
    for j in range(n):

        if grid[i][j] == '*':
            continue

        if i > 0:
            dp[i][j] += (dp[i-1][j] % MOD)

        if j > 0:
            dp[i][j] += (dp[i][j-1] % MOD)

print(dp[n-1][n-1] % MOD)
