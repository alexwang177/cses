import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


MAXD = 30


def jump(parent, a, d):
    for i in range(MAXD):
        if d & (1 << i):
            a = parent[index(a, i)]

    return a


n, q = ria()
adj = ria()


def index(i, j):
    return i * MAXD + j


'''
    parent[i][j] = node i's (2^j)-th parent
'''

parent = [0 for _ in range(n * MAXD + MAXD)]

for i in range(1, n+1):
    parent[index(i, 0)] = adj[i-1]

for d in range(1, MAXD):
    for i in range(1, n+1):
        parent[index(i, d)] = parent[index(parent[index(i, d-1)], d-1)]

for _ in range(q):
    a, d = ria()
    print(jump(parent, a, d))
