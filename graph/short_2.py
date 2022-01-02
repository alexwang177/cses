import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m, q = ria()
adj = {}

for _ in range(m):
    a, b, w = ria()

    if a not in adj:
        adj[a] = []
    if b not in adj:
        adj[b] = []

    adj[a].append(b, w)
    adj[b].append(a, w)

dist = [[0 if i == j else None for i in range(n)] for j in range(n)]

for _ in range(q):
    a, b = ria()
