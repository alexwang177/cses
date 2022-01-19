import sys
from heapq import heappush, heappop

MAX = 1 << 60
MOD = (10**9) + 7


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m = ria()
adj = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b, c = ria()
    adj[a].append((b, c))

dist = [MAX for _ in range(n+1)]
dist[1] = 0

num_routes = [0 for _ in range(n+1)]
num_routes[1] = 1

max_edges = [0 for _ in range(n+1)]
min_edges = [0 for _ in range(n+1)]

visited = set()

# tuple (cur_dist, node)
pq = [(0, 1)]

while pq:
    cur_dist, node = heappop(pq)

    if node in visited:
        continue
    visited.add(node)

    for nei, w in adj[node]:
        if cur_dist + w < dist[nei]:
            dist[nei] = cur_dist + w
            num_routes[nei] = num_routes[node]
            min_edges[nei] = min_edges[node] + 1
            max_edges[nei] = max_edges[node] + 1
            heappush(pq, (cur_dist + w, nei))
        elif cur_dist + w == dist[nei]:
            num_routes[nei] += num_routes[node]
            num_routes[nei] %= MOD
            min_edges[nei] = min(min_edges[nei], min_edges[node] + 1)
            max_edges[nei] = max(max_edges[nei], max_edges[node] + 1)

print(dist[n], num_routes[n], min_edges[n], max_edges[n])
