import sys
import heapq

'''

3
5 8
2 4
3 9

(2,4) (3,9) (5,8)

heap: 

(2, 1) (3, 1) (4, -1) (5, 1) (8, -1) (9, -1)

1 2 1 2 1 0

0  2  3  4  5  8  9

0  1  2  1  2  1  0
'''

n = int(sys.stdin.readline())
arr = []

# Approach 1

# for _ in range(n):
#     arr.append(tuple(int(x) for x in sys.stdin.readline().strip().split(" ")))

# h = []
# ans = 0

# arr.sort(key=lambda x: x[0])

# for x in arr:

#     while h and h[0] <= x[0]:
#         heapq.heappop(h)

#     heapq.heappush(h, x[1])

#     ans = max(ans, len(h))

# Approach 2

for _ in range(n):
    p = tuple(int(x) for x in sys.stdin.readline().strip().split(" "))

    arr.append((p[0], 1))
    arr.append((p[1], -1))

arr.sort(key=lambda x: x[0])

ans = 0
cur = 0

for x in arr:
    cur += x[1]
    ans = max(ans, cur)

print(ans)
