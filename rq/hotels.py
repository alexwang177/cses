import sys


class MaxSegmentTree:

    # tree is one-indexed for convenience

    def __init__(self, arr):

        while not MaxSegmentTree.is_pow_of_2(len(arr)):
            arr.append(1000000007)

        self.n = len(arr)
        n = self.n

        self.tree = [0 for _ in range(2*n)]

        # insert leaf nodes in tree
        for i in range(n):
            self.tree[n+i] = arr[i]

        # create higher level nodes
        for i in range(n-1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

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
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
            i = i // 2

    def get_max(self, l, r):

        # find correct positions in tree array
        l += self.n
        r += self.n

        max_val = max(self.tree[l], self.tree[r])
        idx = 10000007

        while l <= r:

            # print(f"left {self.tree[l]} right {self.tree[r]}")

            # left pointer is right child
            if l % 2 == 1:

                if self.tree[l] > max_val or (self.tree[l] == max_val and l < idx):
                    max_val = self.tree[l]
                    idx = l

                l += 1

            # right pointer is left child
            if r % 2 == 0:

                if self.tree[r] > max_val or (self.tree[r] == max_val and r < idx):
                    max_val = self.tree[r]
                    idx = r

                r -= 1

            # move up one level in tree
            l = l//2
            r = r//2

        return (max_val, idx)


def ria():
    return [int(x) for x in sys.stdin.readline().split()]
