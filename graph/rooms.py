import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def dfs(grid, r, c, n, m):

    s = [(r, c)]

    while s:
        r, c = s.pop()

        if r < 0 or c < 0 or r >= n or c >= m:
            continue

        if grid[r][c] == '#':
            continue

        grid[r][c] = '#'

        s.append((r + 1, c))
        s.append((r, c + 1))
        s.append((r - 1, c))
        s.append((r, c - 1))


n, m = ria()
grid = []

for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))

ans = 0

for i in range(n):
    for j in range(m):

        if grid[i][j] == '.':
            ans += 1
            dfs(grid, i, j, n, m)

print(ans)
