import sys

delta = {
    'D': (1, 0),
    'U': (-1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

visited = [[False for _ in range(7)] for _ in range(7)]


def valid(row, col, visited):
    return row >= 0 and col >= 0 and row <= 6 and col <= 6 and not visited[row][col]


def wall_pos(row, col, visited):

    if (row == 0 or row == 6) and \
            col > 0 and col < 6 and not visited[row][col - 1] and not visited[row][col + 1]:
        return True

    if (col == 0 or col == 6) and \
            row > 0 and row < 6 and not visited[row - 1][col] and not visited[row + 1][col]:
        return True

    return False


def gen_num_paths(path, row, col, idx, visited):

    if idx == 48:
        if row == 6 and col == 0:
            # print("end")
            return 1
        return 0

    if row == 6 and col == 0:
        return 0

    if wall_pos(row, col, visited):
        return 0

    num_paths = 0
    c = path[idx]

    if c == '?':
        for d in delta.values():

            if valid(row + d[0], col + d[1], visited):
                visited[row + d[0]][col + d[1]] = True
                num_paths += gen_num_paths(path, row +
                                           d[0], col + d[1], idx + 1, visited)
                visited[row + d[0]][col + d[1]] = False

    else:
        d = delta[c]

        if valid(row + d[0], col + d[1], visited):
            visited[row + d[0]][col + d[1]] = True
            num_paths += gen_num_paths(path, row +
                                       d[0], col + d[1], idx + 1, visited)
            visited[row + d[0]][col + d[1]] = False

    return num_paths


path = sys.stdin.readline().strip()
visited[0][0] = True
print(gen_num_paths(path, 0, 0, 0, visited))
