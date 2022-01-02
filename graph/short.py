import sys
from heapq import heappush, heappop


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m = ria()
adj = {}

for _ in range(m):
    a, b, w = ria()

    if a not in adj:
        adj[a] = []

    adj[a].append((b, w))

dist = [None for _ in range(n + 1)]
dist[1] = 0

# tuple: (distance, node)
pq = [(0, 1)]
visited = set()

while pq:
    cur_dist, node = heappop(pq)

    if node in visited:
        continue

    visited.add(node)

    if node in adj:
        for nei, w in adj[node]:

            # try to find a better path to neighbor
            if dist[nei] is None or cur_dist + w < dist[nei]:
                dist[nei] = cur_dist + w
                heappush(pq, (dist[nei], nei))

print(*dist[1:])
