import sys

# multiples of 3, same number, works

# other case: numbers are different but we can reach the same multiple of 3

# 10 8
# 8 7
# 6 6

# a - 2x = b - x
# x = a - b

t = int(sys.stdin.readline())

for _ in range(t):

    i, j = tuple(int(x) for x in sys.stdin.readline().split(" "))

    a = max(i, j)
    b = min(i, j)
    x = a - b

    val_1 = a - 2*x
    val_2 = b - x

    if val_1 >= 0 and val_1 % 3 == 0 and val_2 >= 0 and val_2 % 3 == 0:
        print("YES")
    else:
        print("NO")
