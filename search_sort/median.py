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

print(" ")
print(k-1)
print(small)
print(large)
print(" ")

for i in range(k, n):

    x = arr[i]
    prev = i - k

    if x >= large[0][0]:
        # add to large heap
        heapq.heappush(large, (x, i))

        # add to small heap to maintain original heap sizes
        if arr[prev] <= large[0][0]:
            switch(large, small)

    else:
        # add to small heap
        heapq.heappush(small, (-x, i))

        # add to large heap to maintain original heap sizes
        if arr[prev] >= large[0][0]:
            switch(small, large)

    # throw out invalid indices

    while small and small[0][1] <= prev:
        heapq.heappop(small)

    while large and large[0][1] <= prev:
        heapq.heappop(large)

    print(" ")
    print(i)
    print(small)
    print(large)
    print(" ")

    ans.append(get_median(small))

print(*ans)
