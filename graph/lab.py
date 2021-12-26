import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def bfs(grid, n, m, start_r, start_c):

    q = deque([(start_r, start_c, '', 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]

    while q:

        r, c, path, l = q.popleft()

        if r < 0 or c < 0 or r >= n or c >= m:
            continue

        if visited[r][c] or grid[r][c] == '#':
            continue

        if grid[r][c] == 'B':
            return (l, path)

        visited[r][c] = True

        q.append((r + 1, c, path + 'D', l + 1))
        q.append((r - 1, c, path + 'U', l + 1))
        q.append((r, c + 1, path + 'R', l + 1))
        q.append((r, c - 1, path + 'L', l + 1))

    return None


n, m = ria()
grid = []

for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))

ans = None

for i in range(n):
    for j in range(m):

        if grid[i][j] == 'A':
            ans = bfs(grid, n, m, i, j)
            break

if ans:
    l, path = ans
    print("YES")
    print(l)
    print(path)
else:
    print("NO")
