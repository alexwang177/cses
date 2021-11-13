class SegmentTree:

    # tree is one-indexed for convenience

    def __init__(self, arr):

        self.n = len(arr)
        n = self.n

        self.tree = [0 for _ in range(2*n)]

        # insert leaf nodes in tree
        for i in range(n):
            self.tree[n+i] = arr[i]

        # create higher level nodes
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, idx, val):

        # update value in tree array
        n = self.n
        self.tree[idx+n] = val

        i = idx + n

        while i > 1:
            self.tree[i//2] = self.tree[i] + self.tree[i+1]
            i = i//2

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
            l = l//2
            r = r//2

        return sum
