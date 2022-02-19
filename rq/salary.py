from operator import pos
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

    def add(self, idx, val):
        self.update(idx, self.tree[idx + self.n] + val)

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


'''
1) index compress the possible salary values
2) create freq arr and seg tree on that arr
3) answer range queries on tree / do point updates
'''

n, q = ria()
salary = ria()
pos_salaries = set(salary)
queries = []

for _ in range(q):
    t, a, b = sys.stdin.readline().split()
    queries.append([t, int(a), int(b)])

    if t == '?':
        pos_salaries.add(int(a))

    pos_salaries.add(int(b))

pos_salaries = sorted(list(pos_salaries))
compressed = {}

for i, sal in enumerate(pos_salaries):
    compressed[sal] = i

freq = [0 for _ in range(len(compressed))]

for sal in salary:
    freq[compressed[sal]] += 1

tree = SegmentTree(freq)

for t, a, b, in queries:
    if t == '?':
        print(tree.get_sum(compressed[a], compressed[b]))
    elif t == '!':
        a -= 1
        prev_sal = salary[a]
        salary[a] = b

        tree.add(compressed[prev_sal], -1)
        tree.add(compressed[b], 1)
