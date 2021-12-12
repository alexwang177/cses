import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, a, b = ria()
arr = ria()

prefix = [0 for _ in range(n+1)]

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

# prefix[i] = arr[0] + arr[1] + ... + arr[i-2] + arr[i-1]
# prefix[i-b] = arr[0] + ... + arr[i-b-1]
# valid = arr[i-b+1] + ... + arr[i]

# 0 1 2 3 4 5 6 7 8 9 10 11
# 2 3 6 3 1 8 8 7 2 9 3 2
# a = 1, b = 3

ans = float('-inf')
w = deque()

# For reference:
# Entries in window store possible prefix sums of index j < i, that will be subtracted from prefix[i]
# valid j is i - b <= j <= i - a
# we explicitly check for the i - b bound
# we never add j > i - a because we only add i - a to window once we reach i

for i in range(a, n+1):

    # remove invalid entries from window
    while w and w[0][0] < i - b:
        # print(f"i: {i}, w[0][0]: {w[0][0]}")
        w.popleft()

    # remove entries in window bigger than current entry
    while w and w[-1][1] > prefix[i - a]:
        w.pop()

    # add current entry
    w.append((i - a, prefix[i - a]))
    ans = max(ans, prefix[i] - w[0][1])

    print(f"ans: {ans}")
    print(f"i: {i}, {w}")
    print(" ")

print(ans)
