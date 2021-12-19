import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n = int(sys.stdin.readline())
coins = ria()

'''
dp[i][v] = True if we can make value v considering coins [0 ... i-1]

dp[0][v] = False for all v

dp[i][0] = True for all v

dp[i][v] = dp[i-1][v - coins[i-1]]
'''

total = sum(coins)
dp = [[False for _ in range(total + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = True

ans = set()

for i in range(1, n + 1):
    for v in range(total + 1):

        dp[i][v] |= dp[i-1][v]

        coin = coins[i-1]

        if v - coin >= 0:
            dp[i][v] |= dp[i-1][v - coin]

        if dp[i][v] and v > 0:
            ans.add(v)

# for row in dp:
#     print(*row)

ans = sorted(list(ans))

print(len(ans))
print(*ans)
