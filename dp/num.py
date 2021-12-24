import sys
from functools import lru_cache


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


'''

dp[i][d][p][s] = number of valid numbers up for s[0...i], ending with digit d, p denotes if prefix or not, s denotes if started or not

dp[i][d][p][s] = sum ( dp[i-1][d*][p*][s*] ) for valid d* p* s*
where d* != d,

p* determines the range of d values we evaluate,

p is calculated based on p* and d


base case:

dp[0][d][True][s] = 1


pseudocode:

for i in range(n):

    for d in range(10):

        for d* in range(10):

            for p* in [True, False]:

                for s* in [True, False]:

                    if d* == d and not (d == 0 and not started): continue

                    if p* and d > s[i]: continue

                    p = p* and d == int(s[i])

                    s = s* or d

                    dp[i][d][p][s] += dp[i-1][d*][p*][s*]

ans = 0

for d in range(10):
    ans += dp[n-1][d][True]
    ans += dp[n-1][d][False]

return ans

'''


@lru_cache(None)
def solve(s, idx, started, is_prefix, last_digit):

    if idx == len(s):
        return 1

    ans = 0

    for d in range(10 if not is_prefix else int(s[idx]) + 1):
        if d != last_digit or not(d or started):
            ans += solve(s, idx + 1, started or d,
                         is_prefix and d == int(s[idx]), d)

    return ans


a, b = ria()
ans1 = 0 if a == 0 else solve(str(a - 1), 0, False, True, -1)
ans2 = 1 if b == 0 else solve(str(b), 0, False, True, -1)
print(ans2 - ans1)
