import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def dfs(start, visited, parent, adj):

    s = [start]

    while s:

        node = s.pop()
        visited.add(node)

        if node in adj:
            for nei in adj[node]:

                if nei in visited:
                    if node in parent and nei != parent[node]:

                        cycle_start = nei
                        cycle = [cycle_start]
                        cur = node

                        while cur != cycle_start:
                            cycle.append(cur)
                            cur = parent[cur]

                        cycle.append(cycle_start)
                        print(len(cycle))
                        print(*cycle)
                        return True
                else:
                    s.append(nei)
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
        if dfs(i, visited, parent, adj):
            sys.exit()

print("IMPOSSIBLE")
