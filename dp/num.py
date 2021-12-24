import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


'''

dp[i][x] = number of valid numbers of length i, that end with digit x

dp[0][x] = 0

dp[i][x] =  sum ( dp[i-1][y] ) for all y != x, and x <= corresponding digit in the number we want to solve

'''


def solve(num):

    num = str(num)
    n = len(num)

    dp = [[0 for _ in range(10)] for _ in range(n + 1)]

    for x in range(10):
        dp[0][x] = 1

    for i in range(1, n + 1):

        for x in range(10):

            # print(f"i: {i} x: {x}")

            for y in range(10):

                if x == y:
                    continue

                dp[i][x] += dp[i-1][y]

    ans = 0

    # for row in dp:
    #     print(*row)

    for x in range(10):
        ans += dp[n][x]

    return ans


a, b = ria()

print(solve(b) - solve(a - 1))
