import sys
from bisect import bisect_right

'''
5 3
5 3 7 8 5
4 8 3

3 5 5 7 8
'''


class MaxSegmentTree:

    # tree is one-indexed for convenience

    def __init__(self, arr):

        while not MaxSegmentTree.is_pow_of_2(len(arr)):
            arr.append(-1000000007)

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

        while i > 1:
            self.tree[i//2] = max(self.tree[i], self.tree[i+1])
            i = i//2

    def get_max(self, l, r):

        max_val = -1000000007

        # find correct positions in tree array
        l += self.n
        r += self.n

        while l <= r:

            # print(f"left {self.tree[l]} right {self.tree[r]}")

            # left pointer is right child
            if l % 2 == 1:
                max_val = max(max_val, self.tree[l])
                l += 1

            # right pointer is left child
            if r % 2 == 0:
                max_val = max(max_val, self.tree[r])
                r -= 1

            # move up one level in tree
            l = l//2
            r = r//2

        return max_val

    def query(self, l, r):
        max_val = 0

        # to find the sum in the range [l,r)
        l += self.n
        r += self.n

        while l < r:

            if ((l & 1) > 0):
                max_val = max(max_val, self.tree[l])
                l += 1

            if ((r & 1) > 0):
                r -= 1
                max_val = max(max_val, self.tree[r])

            l = l // 2
            r = r // 2

        return max_val


n, m = [int(x) for x in sys.stdin.readline().split(" ")]
ticket = [int(x) for x in sys.stdin.readline().split(" ")]
cust = [int(x) for x in sys.stdin.readline().split(" ")]

ticket.sort()
# print(ticket)
tree = MaxSegmentTree(list(range(n)))

for c in cust:

    # print(" ")

    i = bisect_right(ticket, c)
    # print(tree.tree)

    if i == len(ticket) or ticket[i] > c:
        i -= 1

    # print(f"insertion: {i}")

    if i == -1:
        print(-1)
    else:

        idx = tree.get_max(0, i)
        # print(f"idx: {idx}")

        if idx == -1000000007:
            print(-1)
        else:
            print(ticket[idx])
            tree.update(idx, -1000000007)
