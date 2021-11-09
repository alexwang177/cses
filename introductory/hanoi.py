import sys

n = int(sys.stdin.readline())


def hanoi(n, source, dest, aux):

    if n == 1:
        print(f"{source} {dest}")
    else:
        hanoi(n-1, source, aux, dest)
        print(f"{source} {dest}")
        hanoi(n-1, aux, dest, source)


print(2**n - 1)
hanoi(n, 1, 3, 2)
