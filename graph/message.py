import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def bfs(start, end, adj):

    q = deque([start])
    visited = set()
    prev = {}

    while q:

        node = q.popleft()

        if node == end:
            cur = node
            path = []

            while cur != start:
                path.append(cur)
                cur = prev[cur]

            path.append(start)
            return path[::-1]

        if node in adj:
            for nei in adj[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
                    prev[nei] = node

    return None


n, m = ria()
adj = {}

for _ in range(m):
    a, b = ria()

    if a not in adj:
        adj[a] = []
    if b not in adj:
        adj[b] = []

    adj[a].append(b)
    adj[b].append(a)

ans = bfs(1, n, adj)

if ans:
    print(len(ans))
    print(*ans)
else:
    print("IMPOSSIBLE")
