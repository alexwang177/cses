import sys


def valid(row, col):
    return row >= 0 and col >= 0 and row < 8 and col < 8


def gen_num_ways(board, row):

    if row < 0:
        print("hi")
        return 1

    num_ways = 0

    for col in range(8):

        attack_set = set()

        if board[row][col] == '*':
            continue

        for r in range(8):
            board[r][col] = '*'
            attack_set.add((r, col))

        i, j = row, col

        while valid(i, j):
            board[i][j] = '*'
            attack_set.add((i, j))
            i -= 1
            j -= 1

        i, j = row, col

        while valid(i, j):
            board[i][j] = '*'
            attack_set.add((i, j))
            i -= 1
            j += 1

        num_ways += gen_num_ways(board, row - 1)

        for pos in attack_set:
            board[pos[0]][pos[1]] = '.'

    return num_ways


board = []

for _ in range(8):
    board.append(list(sys.stdin.readline().strip()))

print(gen_num_ways(board, 7))
