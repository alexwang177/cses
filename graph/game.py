import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def topo(adj, back_adj, indegree, dp):

    q = deque([i for i in range(1, n+1) if indegree[i] == 0])

    while q:
        node = q.popleft()

        for nei in adj[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

        for prev in back_adj[node]:
            dp[node] += dp[prev]
            dp[node] %= MOD


MOD = (10**9)+7

n, m = ria()

adj = {i: [] for i in range(1, n+1)}
back_adj = {i: [] for i in range(1, n+1)}

indegree = [0 for _ in range(n+1)]
dp = [1 if i == 1 else 0 for i in range(n+1)]

for _ in range(m):
    a, b = ria()
    adj[a].append(b)
    back_adj[b].append(a)
    indegree[b] += 1

topo(adj, back_adj, indegree, dp)

print(dp[n])
