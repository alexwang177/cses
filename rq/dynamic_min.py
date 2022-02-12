import sys


class MinSegmentTree:

    # tree is one-indexed for convenience

    def __init__(self, arr):

        while not MinSegmentTree.is_pow_of_2(len(arr)):
            arr.append(1000000007)

        self.n = len(arr)
        n = self.n

        self.tree = [0 for _ in range(2*n)]

        # insert leaf nodes in tree
        for i in range(n):
            self.tree[n+i] = arr[i]

        # create higher level nodes
        for i in range(n-1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])

    @classmethod
    def is_pow_of_2(self, num):
        return (num & (num-1) == 0) and num != 0

    def update(self, idx, val):

        # update value in tree array
        n = self.n
        self.tree[idx+n] = val

        i = idx + n
        i = i // 2

        while i >= 1:
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])
            i = i // 2

    def get_min(self, l, r):

        # find correct positions in tree array
        l += self.n
        r += self.n

        min_val = min(self.tree[l], self.tree[r])

        while l <= r:

            # print(f"left {self.tree[l]} right {self.tree[r]}")

            # left pointer is right child
            if l % 2 == 1:
                min_val = min(min_val, self.tree[l])
                l += 1

            # right pointer is left child
            if r % 2 == 0:
                min_val = min(min_val, self.tree[r])
                r -= 1

            # move up one level in tree
            l = l//2
            r = r//2

        return min_val


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n, q = ria()
arr = ria()
tree = MinSegmentTree(arr)

for _ in range(q):
    t, a, b = ria()

    if t == 1:
        tree.update(a-1, b)
    elif t == 2:
        print(tree.get_min(a-1, b-1))
