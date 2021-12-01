import sys
import heapq


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def get_median(small):
    return -small[0][0]


def switch(h1, h2):
    x, i = heapq.heappop(h1)
    heapq.heappush(h2, (-x, i))


n, k = ria()
arr = ria()

if k == 1:
    print(*arr)
    sys.exit()

small, large = [], []

for i in range(k):
    heapq.heappush(small, (-arr[i], i))

for _ in range(k//2):
    switch(small, large)

ans = [get_median(small)]

# print(" ")
# print(k-1)
# print(small)
# print(large)
# print(" ")

for i in range(k, n):

    x = arr[i]
    prev = i - k

    # print(" ")
    # print(i)
    # print(small)
    # print(large)
    # print(" ")

    old_large_top = large[0][0]

    # always push to small (push current to large and then push top of large to small)
    heapq.heappush(large, (x, i))
    switch(large, small)

    if arr[prev] >= old_large_top:
        # num to be removed is in large
        # push top of small to large
        switch(small, large)

    # throw out invalid indices
    while large and large[0][1] <= prev:
        heapq.heappop(large)

    while small and small[0][1] <= prev:
        heapq.heappop(small)

    # print(" ")
    # print(i)
    # print(small)
    # print(large)
    # print(" ")

    ans.append(get_median(small))

print(*ans)
