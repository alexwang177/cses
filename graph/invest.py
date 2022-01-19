import sys
from heapq import heappush, heappop

MAX = 1 << 60


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m = ria()
adj = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b, c = ria()
    adj[a].append((b, c))

dist = [MAX for _ in range(n+1)]
dist[1] = 0

num_routes = 0
max_edges = -1
min_edges = n

# tuple (cur_dist, num_edges, node)
pq = [(0, 0, 1)]

while pq:
    cur_dist, num_edges, node = heappop(pq)

    if node == n:
        min_edges = min(min_edges, num_edges)
        max_edges = max(max_edges, num_edges)
        num_routes += 1

    for nei, w in adj[node]:
        if cur_dist + w <= dist[nei]:
            dist[nei] = cur_dist + w
            heappush(pq, (cur_dist + w, num_edges + 1, nei))

print(dist[n])
print(num_routes)
print(min_edges)
print(max_edges)
