import sys

n = int(sys.stdin.readline())


def get_val(r, c):
    max_idx = max(r, c)
    min_idx = min(r, c)
    corner_val = max_idx**2 - max_idx + 1

    # odd columns are increasing when moving up the rows
    # even columns are decreasing ...

    # odd rows are decreasing when moving left
    # even rows are increasing ...

    if r == c:
        return corner_val

    val = corner_val
    diff = max_idx - min_idx

    if r == c:
        return val
    elif r < c:
        # move up the column

        if c % 2 == 0:
            val -= diff
        else:
            val += diff
    else:
        # move left on the row

        if r % 2 == 0:
            val += diff
        else:
            val -= diff

    return val


for _ in range(n):
    r, c = (int(x) for x in sys.stdin.readline().split(" "))
    print(get_val(r, c))
