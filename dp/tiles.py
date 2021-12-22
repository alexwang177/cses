import sys
from collections import defaultdict


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def gen_strs(strs, s, n):

    if len(s) == n:

        if s[0] != 'd' and s[-1] != 'c':
            strs.append(s)
        return

    if s and s[-1] == 'c':
        gen_strs(strs, s + 'd', n)
    else:
        for ch in 'abc':
            gen_strs(strs, s + ch, n)


def compate(s1, s2):

    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]

        if c1 == 'a' and c2 != 'b':
            return False

        if c2 == 'b' and c1 != 'a':
            return False

    return True


'''
dp[i][x] = number of ways considering rows [0 ... i] and row i has configuration "x"

x is a string

'a' = vertical, top
'b' = vertical, bottom
'c' = horizontal, left
'd' = horizontal, right

dp[i][x] = sum ( dp[i-1][y] ) for all configurations "y" compatible with "x", and "x" is valid 

base case:

dp[0][x] = 1 if "x" is valid
dp[0][x] = 0 if "x" is invalid
'''

n, m = ria()
MOD = (10**9)+7

strs = []
gen_strs(strs, '', n)
# print(strs)

dp = [defaultdict(int) for _ in range(m)]

for i in range(m):

    for s in strs:
        if i == 0 and 'b' not in s:
            dp[i][s] = 1
        elif (i > 0 and i < m - 1) or (i == m - 1 and 'a' not in s):
            for prev in strs:
                if compate(prev, s):
                    dp[i][s] += dp[i-1][prev]
                    dp[i][s] %= MOD

ans = sum(dp[m - 1].values()) % MOD
print(ans)
