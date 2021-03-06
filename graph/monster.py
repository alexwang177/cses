import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


delta = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}


# def monster_bfs(start_r, start_c, aux, grid, n, m):
#     q = deque([(start_r, start_c)])
#     visited = set()
#     level = 0

#     while q:
#         size = len(q)

#         for _ in range(size):
#             r, c = q.popleft()
#             visited.add((r, c))

#             if aux[r][c] is None or aux[r][c] > level:
#                 aux[r][c] = level

#             for dr, dc in delta.values():
#                 nr = r + dr
#                 nc = c + dc

#                 if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] == '#':
#                     continue

#                 if (nr, nc) not in visited:
#                     q.append((nr, nc))

#         level += 1


def bfs(q, grid, n, m):
    level = 0

    while q:
        size = len(q)

        for _ in range(size):
            r, c, p = q.popleft()

            if p == 'A' and (r == 0 or c == 0 or r == n - 1 or c == m - 1):
                print('YES')
                print(level)

                path = []
                while grid[r][c] != 'A':
                    path.append(grid[r][c])
                    dr, dc = delta[grid[r][c]]
                    r -= dr
                    c -= dc

                path.reverse()
                print(*path, sep='')

                return True

            for text, (dr, dc) in delta.items():
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] != '.':
                    continue

                if p == 'A':
                    grid[nr][nc] = text
                elif p == 'M':
                    grid[nr][nc] = p

                q.append((nr, nc, p))

        level += 1

    return False


n, m = ria()
grid = []
aux = []

for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))
    aux.append([None for _ in range(m)])

q = deque([])

start_r, start_c = 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'M':
            q.append((i, j, grid[i][j]))
        elif grid[i][j] == 'A':
            start_r, start_c = i, j

q.append((start_r, start_c, 'A'))

valid = bfs(q, grid, n, m)

if not valid:
    print('NO')

# for row in grid:
#     print(*row)
