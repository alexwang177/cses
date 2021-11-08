import sys


def inbounds(row, col):
    return row >= 0 and col >= 0 and row < 8 and col < 8


def valid(board, row, col):

    if board[row][col] == '*':
        return False

    for r in range(0, row):
        if board[r][col] == 'Q':
            return False

    i, j = row, col

    while inbounds(i, j):
        if board[i][j] == 'Q':
            return False

        i -= 1
        j -= 1

    i, j = row, col

    while inbounds(i, j):
        if board[i][j] == 'Q':
            return False

        i -= 1
        j += 1

    return True


def gen_num_ways(board, row):

    if row == 8:
        return 1

    num_ways = 0

    for col in range(8):

        if valid(board, row, col):

            board[row][col] = 'Q'
            num_ways += gen_num_ways(board, row + 1)
            board[row][col] = '.'

    return num_ways


board = []

for _ in range(8):
    board.append(list(sys.stdin.readline().strip()))

print(gen_num_ways(board, 0))
