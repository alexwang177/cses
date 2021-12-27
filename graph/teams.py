import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def bfs(start, adj, visited):

    flag = 0
    label = {}
    q = deque([start])

    while q:

        size = len(q)

        for _ in range(size):
            node = q.popleft()
            label[node] = flag + 1

            if node in adj:
                for nei in adj[node]:

                    if nei in label and label[nei] == flag + 1:
                        return None

                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        flag ^= 1

    return label


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
ans = {}

for i in range(1, n + 1):

    if i not in visited:
        label = bfs(i, adj, visited)

        if label:
            ans.update(label)
        else:
            print("IMPOSSIBLE")
            sys.exit()

team = []

for i in range(1, n + 1):
    team.append(ans[i])

print(*team)
