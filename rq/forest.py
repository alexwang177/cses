import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def query(dp, coor):
    coor = [v-1 for v in coor]
    y1, x1, y2, x2 = coor

    ans = dp[y2][x2]

    if y1 > 0:
        ans -= dp[y1-1][x2]

    if x1 > 0:
        ans -= dp[y2][x1-1]

    if y1 > 0 and x1 > 0:
        ans += dp[y1-1][x1-1]

    return ans


n, q = ria()
grid = []

for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            dp[i][j] += 1

        if i > 0:
            dp[i][j] += dp[i-1][j]

        if j > 0:
            dp[i][j] += dp[i][j-1]

        if i > 0 and j > 0:
            dp[i][j] -= dp[i-1][j-1]

for _ in range(q):
    coor = ria()
    print(query(dp, coor))
