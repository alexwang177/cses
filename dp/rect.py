import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


a, b = ria()

'''

dp[i][j] = min cuts for i x j rectangle

dp[i][j] = 0 if i == j

dp[i][j] = dp[u][v] + dp[i - u][j - v] for all valid u, v 


dp[3][5] = dp[3][3] + dp[3][2]

dp[3][2] = dp[2][2] + dp[1][2]

dp[1][2] = dp[1][1] + dp[1][1]

'''

MAX = (10**9)+7
n = 501
dp = [[MAX for _ in range(n)] for _ in range(n)]

if a == b:
    print(0)
    sys.exit()

for i in range(n):

    for j in range(n):

        if i == j:
            dp[i][j] = 0
            continue

        if i >= j:
            dp[i][j] = dp[j][i]
            continue

        for k in range(1, i):
            dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1)

        for k in range(1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k] + 1)

# for row in dp:
#     print(row)
print(dp[a][b])
