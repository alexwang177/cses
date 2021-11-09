import sys

n = int(sys.stdin.readline())

for k in range(1, n+1):
    print(((k**2 * (k**2 - 1)) // 2) - (4 * (k-2) * (k-1)))
