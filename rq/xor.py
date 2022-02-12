import sys


class GenSegmentTree:

    # tree is one-indexed for convenience

    def __init__(self, arr, f):

        while not GenSegmentTree.is_pow_of_2(len(arr)):
            arr.append(0)

        self.n = len(arr)
        n = self.n

        self.tree = [0 for _ in range(2*n)]
        self.f = f

        # insert leaf nodes in tree
        for i in range(n):
            self.tree[n+i] = arr[i]

        # create higher level nodes
        for i in range(n-1, 0, -1):
            self.tree[i] = self.f(self.tree[2*i], self.tree[2*i+1])

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
            self.tree[i] = self.f(self.tree[2*i], self.tree[2*i+1])
            i = i // 2

    def get_result(self, l, r):

        # find correct positions in tree array
        l += self.n
        r += self.n

        # ans = self.f(self.tree[l], self.tree[r])
        ans = 0

        while l <= r:

            # print(f"left {self.tree[l]} right {self.tree[r]}")

            # left pointer is right child
            if l % 2 == 1:
                ans = self.f(ans, self.tree[l])
                l += 1

            # right pointer is left child
            if r % 2 == 0:
                ans = self.f(ans, self.tree[r])
                r -= 1

            # move up one level in tree
            l = l//2
            r = r//2

        return ans


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def xor(a, b):
    return a ^ b


n, q = ria()
arr = ria()
tree = GenSegmentTree(arr, lambda a, b: a ^ b)

for _ in range(q):
    a, b = ria()
    print(tree.get_result(a-1, b-1))
