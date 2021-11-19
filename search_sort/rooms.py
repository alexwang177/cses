import sys
import heapq
# from collections import deque

n = int(sys.stdin.readline())
cust = []

for i in range(n):
    cust.append(([int(x) for x in sys.stdin.readline().split()] + [i]))

cust.sort(key=lambda x: x[0])

h = []
max_rooms = 0
# q = deque()
ans = [0 for _ in range(n)]

for c in cust:

    # Check if current customer can replace anybody in heap
    if h and h[0][0] < c[0]:
        last_room = ans[heapq.heappop(h)[1]]
        ans[c[2]] = last_room
        heapq.heappush(h, (c[1], c[2]))
    else:
        heapq.heappush(h, (c[1], c[2]))
        ans[c[2]] = len(h)

    max_rooms = max(max_rooms, len(h))

print(max_rooms)
print(*ans)
