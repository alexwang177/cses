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

# base case
dp = [[n + 1, 0] for _ in range(1 << n)]
dp[0] = [1, 0]

for s in range(1 << n):

    for p in range(n):

        if s & (1 << p):

            prev = dp[s ^ (1 << p)]
            min_trips = prev[0]
            cur_elevator = prev[1]

            if cur_elevator + weight[p] <= cap:
                cur_elevator += weight[p]
            else:
                min_trips += 1
                cur_elevator = weight[p]

            dp[s] = min(dp[s], [min_trips, cur_elevator])

# print(dp)
print(dp[(1 << n) - 1][0])
