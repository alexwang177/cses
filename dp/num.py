import sys
from functools import lru_cache


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


'''
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
