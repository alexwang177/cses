import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m = ria()
adj = {i: [] for i in range(1, n+1)}
indegree = {i: 0 for i in range(1, n+1)}

for _ in range(m):
    a, b = ria()
    adj[a].append(b)
    indegree[b] += 1

q = deque([i for i in range(1, n+1) if indegree[i] == 0])
visited = set()
ans = []

while q:
    c = q.popleft()
    ans.append(c)
    visited.add(c)

    for nei in adj[c]:
        indegree[nei] -= 1

        if indegree[nei] == 0 and nei not in visited:
            q.append(nei)

if len(ans) == n:
    print(*ans)
else:
    print('IMPOSSIBLE')
