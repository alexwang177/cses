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

dist = [[None for _ in range(2)] for _ in range(n + 1)]
dist[1][0] = 0
dist[1][1] = 0

# (cur_dist, node, used)
pq = [(0, 1, False)]
visited = set()

while pq:

    # print(pq)

    cur_dist, node, used = heappop(pq)

    if (node, used) in visited:
        continue

    visited.add((node, used))

    if node in adj:
        for nei, w in adj[node]:

            if not used:
                if dist[nei][True] is None or cur_dist + (w // 2) < dist[nei][True]:
                    dist[nei][True] = cur_dist + (w // 2)
                    heappush(pq, (cur_dist + (w // 2), nei, True))

            if dist[nei][used] is None or cur_dist + w < dist[nei][used]:
                dist[nei][used] = cur_dist + w
                heappush(pq, (cur_dist + w, nei, used))

# print(" ")

# for i in range(1, n + 1):
#     print(f"{i} {dist[i]}")

print(dist[n][1])
