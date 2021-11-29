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

small, large = [], []

for i in range(k):
    heapq.heappush(small, (-arr[i], i))

for _ in range(k//2):
    switch(small, large)

ans = [get_median(small)]

for i in range(k, n):

    x = arr[i]
    prev = i - k

    if x >= large[0][0]:
        heapq.heappush(large, (x, i))

        # element to 'remove' is in small heap, so we need to add more to small heap
        if arr[prev] <= large[0][0]:
            switch(large, small)

    else:
        heapq.heappush(small, (-x, i))

        if arr[prev] >= large[0][0]:
            switch(small, large)

    while small and small[0][1] <= prev:
        heapq.heappop(small)

    while large and large[0][1] <= prev:
        heapq.heappop(large)

    # print(" ")
    # print(i)
    # print(small)
    # print(large)
    # print(" ")

    ans.append(get_median(small))

print(*ans)
