import sys
from math import ceil
from math import log2


class PopulationTree:

    # tree is one-indexed for convenience

    def __init__(self, num_items):

        self.n = 2**(ceil(log2(num_items)))
        n = self.n

        self.tree = [0 for _ in range(2*n)]

        # insert leaf nodes in tree
        for i in range(num_items):
            self.tree[n+i] = 1

        # create higher level nodes
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def delete(self, idx):

        # update value in tree array
        n = self.n
        self.tree[idx+n] = 0

        i = idx + n
        i >>= 1

        while i >= 1:
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
            i >>= 1

    # positions start at 1
    def get_mth_pos(self, m):

        if m <= 0 or m > self.tree[1]:
            return None

        i = 1

        # keep looping until you hit a leaf node
        while i < self.n:
            if m > self.tree[i << 1]:
                m -= self.tree[i << 1]
                i = i << 1 | 1
            else:
                i = i << 1

        # return leaf node's actual index
        return i - self.n


n, k = [int(x) for x in sys.stdin.readline().split(" ")]
tree = PopulationTree(n)
pos = 0
ans = []

'''
n = 7
k = 2
pos = 0

1 2 3 4 5 6 7
l = 7
pos = (0 + 3) % 7 = 3
v (original index) = 2
ans = 3

1 2 4 5 6 7
l = 6
pos = (2 + 3) % 6 = 5
v = 5
ans = 6

1 2 4 5 7
l = 5
pos = (4 + 3) % 5 = 2
v = 1
ans = 2

1 4 5 7
l = 4
pos = (1 + 3) % 4 = 0 -> 4
v = 6
ans = 7

1 4 5 7
1 2 3 4

go from "7" to "5"

originally at position 4, 

1 4 5
l = 3
pos = (3 + 3) % 3 = 0 -> 3
v = 4
ans = 5

1 4
l = 2
pos = (2 + 3) % 2 = 1
v = 0
ans = 1

4
l = 1
pos = (0 + 3) % 1 = 3
v = 3
ans = 4

'''

for l in range(n, 0, -1):

    pos = (pos + k + 1) % l

    # print(f"pos {pos} length {l}")

    if pos == 0:
        pos = l

    v = tree.get_mth_pos(pos)
    # print(v, tree.tree)

    ans.append(v+1)
    tree.delete(v)
    pos -= 1

    # print(" ")

print(*ans)
