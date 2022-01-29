import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, q = ria()
arr = ria()

prefix = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

for _ in range(q):
    a, b = ria()
    print(prefix[b] - prefix[a - 1])
