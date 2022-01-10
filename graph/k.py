import sys
from heapq import heappush, heappop


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, m, k = ria()
adj = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b, w = ria()
    adj[a].append((b, w))

# (cur_dist, node)
pq = [(0, 1)]
cnt = [0 for _ in range(n + 1)]
ans = []

while pq and cnt[n] < k:
    cur_dist, node = heappop(pq)
    cnt[node] += 1

    if cnt[node] > k:
        continue

    if node == n:
        ans.append(cur_dist)

    for nei, w in adj[node]:
        heappush(pq, (cur_dist + w, nei))

print(*ans)
