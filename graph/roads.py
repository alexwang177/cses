import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def dfs(start_c, adj, visited):

    s = [start_c]

    while s:

        c = s.pop()

        if c in visited:
            continue

        visited.add(c)

        if c in adj:
            for nei in adj[c]:
                s.append(nei)


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

components = []
visited = set()

for c in range(1, n + 1):

    if c not in visited:
        dfs(c, adj, visited)
        components.append(c)

print(len(components) - 1)

for i in range(len(components) - 1):
    print(f"{components[i]} {components[i+1]}")
