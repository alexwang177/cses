import sys
import heapq


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, k = ria()
arr = ria()

small, large = [], []

for i in range(k):
    heapq.heappush(small, (-arr[i], i))

for i in range(k//2):
    x, i = heapq.heappop(small)
    heapq.heappush(large, (-x, i))

ans = []

for i in range(k, n):
    pass

print(*ans)
