import sys


class SegmentTree:

    # tree is one-indexed for convenience
    # as in, tree[0] does not have any meaning

    def __init__(self, arr):

        while not SegmentTree.is_pow_of_2(len(arr)):
            arr.append(0)

        self.n = len(arr)
        n = self.n

        self.tree = [0 for _ in range(2*n)]

        # insert leaf nodes in tree
        for i in range(n):
            self.tree[n+i] = arr[i]

        # create higher level nodes
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    @classmethod
    def is_pow_of_2(self, num):
        return (num & (num-1) == 0) and num != 0

    # idx is 0-indexed
    def update(self, idx, val):

        # update value in tree array
        n = self.n
        self.tree[idx+n] = val

        i = idx + n
        i = i // 2

        while i >= 1:
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
            i = i // 2

    # l and r are 0-indexed indicies
    def get_sum(self, l, r):

        # find correct positions in tree array
        l += self.n
        r += self.n
        ans = 0

        while l <= r:

            # print(f"left {self.tree[l]} right {self.tree[r]}")

            # left pointer is right child
            if l % 2 == 1:
                ans += self.tree[l]
                l += 1

            # right pointer is left child
            if r % 2 == 0:
                ans += self.tree[r]
                r -= 1

            # move up one level in tree
            l = l//2
            r = r//2

        return ans


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def find_org_index(r, n, present, tree):
    lo = 0
    hi = n - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        alive = tree.get_sum(0, mid)

        if alive == r:
            if present[mid]:
                return mid
            else:
                hi = mid
        elif alive < r:
            lo = mid + 1
        else:
            hi = mid

    return lo


n = int(sys.stdin.readline())
arr = ria()
remove = ria()
present = [1 for _ in range(n)]
tree = SegmentTree(present)

for r in remove:
    i = find_org_index(r, n, present, tree)

    tree.update(i, 0)
    present[i] = 0

    print(arr[i])
