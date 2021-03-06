import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


MAX = 1 << 60


def dfs(start, target_set, adj, dist):
    s = [start]
    visited = set()

    while s:

        node = s.pop()

        if node in target_set and dist[node] < MAX:
            return True

        visited.add(node)

        if node in adj:
            for nei in adj[node]:
                if nei not in visited:
                    s.append(nei)

    return False


n, m = ria()
adj = {}
edges = []

for _ in range(m):
    a, b, w = ria()
    edges.append((a, b, -w))

    if b not in adj:
        adj[b] = []

    adj[b].append(a)

dist = [MAX for _ in range(n + 1)]
dist[1] = 0

# bellman ford, n-1 iterations
for _ in range(n):
    for a, b, w in edges:

        if dist[a] == MAX:
            continue

        dist[b] = min(dist[b], dist[a] + w)

# n-th interation checks for negative cycle
cycle_node_set = set()

for a, b, w in edges:
    if dist[a] + w < dist[b]:
        cycle_node_set.add(a)
        cycle_node_set.add(b)

reachable = dfs(n, cycle_node_set, adj, dist)
# print(dist)

print(-1 if reachable else -dist[n])
