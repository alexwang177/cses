import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


MIN = -(1 << 60)


def topo(adj, back_adj, indegree, dist, parent):
    q = deque([i for i in range(1, n+1) if indegree[i] == 0])

    while q:
        node = q.popleft()

        for nei in adj[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

        # dp

        mx = MIN
        mx_node = None

        for prev in back_adj[node]:
            if mx is None or dist[prev] + 1 > mx:
                mx = dist[prev] + 1
                mx_node = prev

        dist[node] = mx

        # edge case, distance to starting city is always 0
        if node == 1:
            dist[node] = 0

        parent[node] = mx_node


n, m = ria()
adj = {i: [] for i in range(1, n+1)}
back_adj = {i: [] for i in range(1, n+1)}
indegree = [0 for _ in range(n+1)]

dist = [MIN for _ in range(n+1)]
parent = [None for _ in range(n+1)]

for _ in range(m):
    a, b = ria()

    adj[a].append(b)
    indegree[b] += 1
    back_adj[b].append(a)

topo(adj, back_adj, indegree, dist, parent)

ans = []
cur = n

while cur != 1:
    ans.append(cur)

    if cur is not None:
        cur = parent[cur]
    else:
        print('IMPOSSIBLE')
        sys.exit()

ans.append(1)
ans.reverse()
print(len(ans))
print(*ans)
