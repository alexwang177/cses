from math import ceil
from math import log2

n, k = map(int, input().strip().split())
N = 2**(ceil(log2(n)))

tree = [0] * 2 * N


def build():
    for i in range(N, N+n):
        tree[i] = 1

    for i in range(N - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]


def deleteValue(p):

    # set value at position p
    tree[p + N] = 0
    p = p + N

    # move upward and update parents
    i = p

    while i > 1:

        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1

# pos start at 1


def getmthpos(m):
    if m <= 0 or m > tree[1]:
        return None
    i = 1
    while i < N:
        # print(i)
        if m > tree[i << 1]:
            m -= tree[i << 1]
            i = i << 1 | 1
        else:
            i = i << 1
    return i-N


build()
ans = []
pos = 0
for l in range(n, 0, -1):
    pos = (pos + k + 1) % l
    if pos == 0:
        pos = l
    # print(pos,tree[1])
    v = getmthpos(pos)
    # print(v)
    ans.append(v+1)
    deleteValue(v)
    pos -= 1

print(*ans)
