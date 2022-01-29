import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


'''

1) multiply by 2 if 2*x < end

2) add one if 

'''


def bfs(start, end):
    q = deque([(start, 0)])

    visited = set()

    while q:
        x, level = q.popleft()

        if x == 0:
            continue

        visited.add(x)
        # print(x)

        if x == end:
            return level

        if x * 2 <= end and x * 2 not in visited:
            q.append((x * 2, level + 1))

        if x + 1 not in visited:
            q.append((x + 1, level + 1))

        if x % 2 == 0 and x // 2 not in visited:
            q.append((x // 2, level + 1))


n = int(sys.stdin.readline())

for _ in range(n):
    a, b = ria()
    ans = 0

    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        ans += 1

    print(ans + bfs(a, b))
