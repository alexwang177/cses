import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def dfs(start, visited, parent, adj):

    s = [start]

    while s:

        node = s.pop()

        if node in adj:
            for nei in adj[node]:

                if nei in visited:
                    if node in parent and parent[node] != nei:
                        print(node)
                        return True
                else:
                    s.append(nei)
                    visited.add(nei)
                    parent[nei] = node

    return False


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

visited = set()
parent = {}

for i in range(n+1):
    if i not in visited:
        print(dfs(i, visited, parent, adj))
