import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m = ria()
edges = []

for _ in range(m):
    a, b, w = ria()
    edges.append((a, b, w))

dist = [None for _ in range(n + 1)]
p = [None for _ in range(n + 1)]
dist[1] = 0

flag = None

for _ in range(n + 1):
    flag = -1

    for a, b, w in edges:
        if dist[b] is None or (dist[a] and dist[b] > dist[a] + w):
            dist[b] = dist[a] + w
            p[b] = a
            flag = b

if flag == -1:
    print("NO")
else:
    print("YES")
