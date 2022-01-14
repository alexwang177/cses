import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


ENTER = 0
EXIT = 1

WHITE = 0
GREY = 1
BLACK = 2


def dfs(start, parent, state, adj):
    s = [(start, ENTER)]

    while s:
        node, action = s.pop()

        if action == EXIT:
            # print(f"EXIT {node}")
            state[node] = BLACK
        else:
            # print(f"ENTER {node}")
            state[node] = GREY
            s.append((node, EXIT))

            for nei in adj[node]:
                if state[nei] == GREY:

                    # print(parent)

                    cycle_start = nei
                    cur = node
                    cycle = [cycle_start]

                    while cur != cycle_start:
                        cycle.append(cur)
                        cur = parent[cur]

                    cycle.append(cycle_start)
                    cycle.reverse()
                    print(len(cycle))
                    print(*cycle)

                    return True
                elif state[nei] == WHITE:
                    s.append((nei, ENTER))
                    parent[nei] = node

    return False


n, m = ria()
adj = {i: [] for i in range(1, n+1)}
state = {i: WHITE for i in range(1, n+1)}
parent = {}

for _ in range(m):
    a, b = ria()
    adj[a].append(b)

for i in range(1, n+1):
    if state[i] == WHITE:
        if dfs(i, parent, state, adj):
            sys.exit()

print("IMPOSSIBLE")
