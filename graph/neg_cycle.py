import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m = ria()
edges = []

MAX = 1 << 60

for _ in range(m):
    a, b, w = ria()
    edges.append((a, b, w))

dist = [MAX for _ in range(n + 1)]
p = [None for _ in range(n + 1)]
dist[1] = 0

flag = None

for _ in range(n + 1):
    flag = -1

    for a, b, w in edges:
        if dist[b] > dist[a] + w:
            dist[b] = dist[a] + w
            p[b] = a
            flag = b

if flag == -1:
    print("NO")
else:
    print("YES")

    node = flag
    visited = set()
    cycle = []

    final_node = None

    while True:
        if node in visited:
            cycle.append(node)
            final_node = node
            break

        visited.add(node)
        cycle.append(node)
        node = p[node]

    idx = cycle.index(final_node)
    cycle = cycle[idx::]

    cycle.reverse()
    print(*cycle)

    # for i in range(1, n + 1):
    #     print(f"{i} -> {p[i]}")
