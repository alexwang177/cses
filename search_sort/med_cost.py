import sys
import heapq


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def get_cost(large_sum, small_sum, k):
    return large_sum - small_sum + median if k % 2 == 1 else large_sum - small_sum


def get_median(small):
    return -small[0][0]


def switch(h1, h2):
    x, i = heapq.heappop(h1)
    heapq.heappush(h2, (-x, i))

    return abs(x)


n, k = ria()
arr = ria()

if k == 1:
    for _ in range(n):
        print("0", sep=" ")

    sys.exit()

small_sum, large_sum = 0, 0
small, large = [], []

for i in range(k):
    heapq.heappush(small, (-arr[i], i))
    small_sum += arr[i]

for _ in range(k//2):
    t = switch(small, large)
    large_sum += t
    small_sum -= t

median = get_median(small)
ans = [get_cost(large_sum, small_sum, k)]

'''
if k is even, small and large have k/2 elements

if k is odd, small has k//2 + 1 elements, odd has k//2 elements
'''

for i in range(k, n):

    x = arr[i]
    prev = i - k

    old_large_top = large[0][0]

    # always push to small (push current to large and then push top of large to small)
    heapq.heappush(large, (x, i))
    large_sum += x

    t = switch(large, small)
    small_sum += t
    large_sum -= t

    if arr[prev] >= old_large_top:

        large_sum -= arr[prev]

        # num to be removed is in large
        # push top of small to large
        t = switch(small, large)
        large_sum += t
        small_sum -= t
    else:
        small_sum -= arr[prev]

    # throw out invalid indices
    while large and large[0][1] <= prev:
        heapq.heappop(large)

    while small and small[0][1] <= prev:
        heapq.heappop(small)

    median = get_median(small)
    ans.append(get_cost(large_sum, small_sum, k))

print(*ans)
