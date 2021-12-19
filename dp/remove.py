import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n = int(sys.stdin.readline())
arr = ria()

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = arr[i]

for l in range(n-1, -1, -1):

    for r in range(l, n):

        if l == r:
            continue

        dp[l][r] = max(arr[l] - dp[l+1][r], arr[r] - dp[l][r-1])

# sum = score_1 + score_2
# sum + (score_1 - score_2) = 2*score_1
# sum / 2 = score_2

ans = (sum(arr) + dp[0][n-1]) // 2
print(ans)

'''

dp[l][r] = maximum of (score_1 - score_2)

dp[l][r] = arr[l] if l == r

dp[l][r] = max(

    arr[l] - dp[l+1][r]

    dp[l+1][r] = score_2 - score_1 (on the interval l+1, r) because player 2 starts

    -dp[l+1][r] = -(score_2 - score_1) = score_1 - score_2

    ----------------------------------------------------------------------------

    arr[r] - dp[l][r-1]

    symmetric to the case above
)

-------------------------------------------------------------------------------

dp[i][j][t] = max score given arr[i ... j] and moving t = 0,1 (first or second)

dp[i][j][t] = max (

    dp[i + 1][j][t^1] + arr[i] 

    dp[i][j - 1][t^1] + arr[j] 

)

base case:

dp[i][j][0] = arr[i] if i == j

'''
