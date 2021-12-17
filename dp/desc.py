import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m = ria()
arr = ria()

'''

dp[i][v] = number of combos from index [0 ... i] and assuming we use value v for arr[i]


if v is given 
dp[i][v] = dp[i-1][v-1] + dp[i-1][v] + dp[i-1][v+1] 

if v = 0
dp[i][v] = sum ( dp[i-1][u] ) for all u [1 ... m] 

base case:
dp[i][v] = 1 if i = 0, for all v [1 ... m]

'''

MOD = (10**9)+7

dp = [[0 for _ in range(m + 1)] for _ in range(n)]

if arr[0] == 0:
    for v in range(1, m + 1):
        dp[0][v] = 1
else:
    dp[0][arr[0]] = 1

for i in range(1, n):

    if arr[i] == 0:
        for v in range(1, m + 1):

            a = dp[i-1][v-1] if v > 1 else 0
            b = dp[i-1][v]
            c = dp[i-1][v+1] if v < m else 0

            dp[i][v] += (a + b + c)
            dp[i][v] %= MOD
    else:

        v = arr[i]

        a = dp[i-1][v-1] if v > 1 else 0
        b = dp[i-1][v]
        c = dp[i-1][v+1] if v < m else 0

        dp[i][v] += (a + b + c)
        dp[i][v] %= MOD

ans = 0

for v in range(1, m + 1):
    ans += dp[n-1][v]
    ans %= MOD

print(ans)
