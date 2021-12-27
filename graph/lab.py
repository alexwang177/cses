import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def bfs(grid, n, m, start_r, start_c):

    q = deque([(start_r, start_c)])
    directions = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

    while q:
        r, c = q.popleft()

        for d, (dr, dc) in directions.items():

            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue

            if grid[nr][nc] == '.':
                q.append((nr, nc))
                grid[nr][nc] = d

            if grid[nr][nc] == 'B':
                path = [d]

                while grid[r][c] != 'A':
                    d = grid[r][c]
                    path.append(d)
                    dr, dc = directions[d]
                    r -= dr
                    c -= dc

                return (len(path), ''.join(reversed(path)))

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
