import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def monster_bfs(start_r, start_c, aux, grid, n, m):
    q = deque([(start_r, start_c)])
    level = 0

    while q:
        size = len(q)

        for _ in range(size):
            r, c = q.popleft()

            if not aux[r][c] or aux[r][c] > level:
                aux[r][c] = level

            for dr, dc in delta:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] == '#':
                    continue

                q.append((nr, nc))

        level += 1


n, m = ria()
grid = []
aux = []

for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))
    aux.append([None for _ in range(m)])

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'M':
            monster_bfs(i, j, aux, n, m)
