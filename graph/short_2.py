import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def ria_opt():
    return map(int, sys.stdin.readline().split())


def get_index(i, j):
    return i + 500 * j


n, m, q = ria()
MAX = 1 << 60
dist = [MAX]*250000

for _ in range(m):
    a, b, w = ria_opt()
    a -= 1
    b -= 1

    idx1 = get_index(a, b)
    idx2 = get_index(b, a)

    dist[idx1] = min(dist[idx1], w)
    dist[idx2] = min(dist[idx2], w)

for i in range(n):
    dist[get_index(i, i)] = 0

for k in range(n):
    for i in range(n):

        if k == i or dist[get_index(i, k)] == MAX:
            continue

        for j in range(i):
            new_dist = dist[get_index(i, k)] + dist[get_index(k, j)]

            if new_dist < dist[get_index(i, j)]:
                dist[get_index(i, j)] = dist[get_index(j, i)] = new_dist

ans = []
for _ in range(q):
    a, b = ria_opt()
    a -= 1
    b -= 1
    ans.append(-1 if dist[get_index(a, b)] == MAX else dist[get_index(a, b)])

print(*ans)
