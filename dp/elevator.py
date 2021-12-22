import sys

'''

dp[s] = [min_trips, current_elevator_weight]

dp[s] = [dp[s*].min_trips, dp[s*].weight + p.weight]

    if person p doesn't overflow current elevator

else

[dp[s*].min_trips + 1, p.weight]

'''


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, cap = ria()
weight = ria()
m = 1 << n

dp = [n + 1 for _ in range(m)]
cw = [0 for _ in range(m)]

# base case
dp[0] = 1

for s in range(1, m):

    for p in range(n):

        if s & (1 << p):

            prev = s ^ (1 << p)
            min_trips = dp[prev]
            cur_w = cw[prev]

            if cur_w + weight[p] <= cap:
                cur_w += weight[p]
            else:
                min_trips += 1
                cur_w = weight[p]

            if min_trips < dp[s] or (min_trips == dp[s] and cur_w < cw[s]):
                dp[s] = min_trips
                cw[s] = cur_w

print(dp[m - 1])
