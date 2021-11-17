import sys
import functools
from math import ceil
from math import log2


class SegmentTree:

    # tree is one-indexed for convenience

    def __init__(self, num_items):

        self.n = 2**(ceil(log2(num_items)))
        n = self.n

        self.tree = [0 for _ in range(2*n)]

        # insert leaf nodes in tree
        for i in range(num_items):
            self.tree[n+i] = 0

        # create higher level nodes
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def increment(self, idx, k):
        # update value in tree array
        n = self.n
        self.tree[idx+n] += k

        i = idx + n
        i >>= 1

        while i >= 1:
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
            i >>= 1

    def update(self, idx, val):

        # update value in tree array
        n = self.n
        self.tree[idx+n] = val

        i = idx + n
        i >>= 1

        while i >= 1:
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
            i >>= 1

    def sum(self, l, r):

        sum = 0

        # find correct positions in tree array
        l += self.n
        r += self.n

        while l <= r:

            # left pointer is right child
            if l % 2 == 1:
                sum += self.tree[l]
                l += 1

            # right pointer is left child
            if r % 2 == 0:
                sum += self.tree[r]
                r -= 1

            # move up one level in tree
            l >>= 1
            r >>= 1

        return sum


def customsort1(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]

    return a[0] - b[0]


n = int(sys.stdin.readline())
ranges = []
nums = set()

for i in range(n):
    l, r = [int(x) for x in sys.stdin.readline().split(" ")]
    ranges.append([l, r, i])
    nums.add(l)
    nums.add(r)

nums = sorted(list(nums))
N = len(nums)
num_map = {nums[i]: i for i in range(N)}

# print(num_map)

count = [0] * n
ranges.sort(key=functools.cmp_to_key(customsort1))

tree1 = SegmentTree(N)

# Contains
for r in ranges[::-1]:
    idx = r[2]
    a = num_map[r[0]]
    b = num_map[r[1]]

    # we have already iterated over ranges that start after us
    # get the number of ranges that end at or before our end
    count[idx] = tree1.sum(a, b)

    tree1.increment(b, 1)

print(*count)

tree2 = SegmentTree(N)

# Contained
for r in ranges:
    idx = r[2]
    a = num_map[r[0]]
    b = num_map[r[1]]

    # we have already iterated over ranges that start before us
    # get the number of ranges that end at or after our end
    count[idx] = tree2.sum(b, N)
    tree2.increment(b, 1)

    # print(r)
    # print(b)
    # print(tree2.tree)

print(*count)
