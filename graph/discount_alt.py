import sys
from heapq import heappush, heappop


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def dijk(start, dist, adj):
    dist[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        cur_dist, node = heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node in adj:
            for nei, w in adj[node]:
                if dist[nei] is None or cur_dist + w < dist[nei]:
                    dist[nei] = cur_dist + w
                    heappush(pq, (cur_dist + w, nei))


n, m = ria()
adj_s = {}
adj_e = {}

for _ in range(m):
    a, b, w = ria()

    if a not in adj_s:
        adj_s[a] = []
    if b not in adj_e:
        adj_e[b] = []

    adj_s[a].append((b, w))
    adj_e[b].append((a, w))

ds = [None for _ in range(n+1)]
de = [None for _ in range(n+1)]

dijk(1, ds, adj_s)
dijk(n, de, adj_e)

ans = None

for a in range(1, n + 1):
    if a in adj_s:
        for b, w in adj_s[a]:

            if ds[a] is None or de[b] is None:
                continue

            if ans is None or (w // 2) + ds[a] + de[b] < ans:
                ans = (w // 2) + ds[a] + de[b]

print(ans)
