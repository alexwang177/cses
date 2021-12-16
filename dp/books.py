import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, budget = ria()
prices = ria()
pages = ria()

dp = [0 for _ in range(budget + 1)]

'''

 0 1 2 2

 1 4 5 8

 2 7 8 1 2

'''

for i in range(n):
    price = prices[i]
    page_count = pages[i]

    for j in range(budget, price - 1, -1):
        dp[j] = max(dp[j], dp[j - price] + page_count)

print(dp[budget])

# dp[j] = most pages you can get with a budget of j


# # dp[i][j] = most pages you can get with a budget of j, considering books [0, i-1] (not including book i)
# dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

# for i in range(1, n + 1):

#     for j in range(budget + 1):

#         # i - 1 is the current book

#         if j - price[i - 1] < 0:
#             # skip this book
#             dp[i][j] = dp[i-1][j]
#         else:
#             # take this book
#             dp[i][j] = max(
#                 dp[i-1][j], dp[i-1][j - price[i-1]] + pages[i-1])

# print(dp[n][budget])
