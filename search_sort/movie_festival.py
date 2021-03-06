import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


class Node:
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data


class BST:

    def __init__(self):
        self.root = None
        self.node_count = 0

    def contains(self, val):

        node = self.root

        while node:

            if val == node.data:
                return True
            elif val < node.data:
                node = node.left
            else:
                node = node.right

        return False

    def add(self, val):

        if self.root == None:
            self.root = Node(None, None, val)
            return

        node = self.root
        prev = None

        while node:

            prev = node

            if val <= node.data:
                node = node.left
            else:
                node = node.right

        node = Node(None, None, val)

        if val <= prev.data:
            prev.left = node
        else:
            prev.right = node

    def remove(self, val):

        if self.contains(val):
            self.root = self._remove(self.root, val)
            return True
        else:
            return False

    def _remove(self, node, val):

        if not node:
            return None

        if val < node.data:
            node.left = self._remove(node.left, val)
        elif val > node.data:
            node.right = self._remove(node.right, val)
        else:

            if not node.left:

                right_child = node.right
                node.data = None
                node = None
                return right_child

            elif not node.right:

                left_child = node.left
                node.data = None
                node = None
                return left_child

            else:

                tmp = self.find_min(node.right)
                node.data = tmp.data
                node.right = self._remove(node.right, tmp.data)

        return node

    def find_min(self, node):
        while node.left:
            node = node.left

        return node

    def find_max_value_with_ceil(self, val):

        node = self.root
        max_val = None

        while node:
            if node.data <= val:
                max_val = node.data
                node = node.right
            else:
                node = node.left

        return max_val

    def print_inorder(self, node):

        if node == None:
            return

        self.print_inorder(node.left)
        print(node.data, sep="")
        self.print_inorder(node.right)

    def print_tree(self):
        self.print_inorder(self.root)


'''

*** optimal = earliest ending

1) assign the k people the k optimal movies

2) for each person, find the next optimal movie that starts after their current movie ends.

3) continue until all movie choices are exhausted

We need O(nlogn) time or better

'''

n, k = ria()
movies = []

for _ in range(n):
    movies.append(ria())

movies.sort(key=lambda x: x[1])
print(movies)

tree = BST()

ans = 0
for i in range(k):
    tree.add(1)

for i in range(n):
    start = movies[i][0]
    end = tree.find_max_value_with_ceil(start)

    if end:
        ans += 1
        tree.remove(end)
        tree.add(movies[i][1])

print(ans)
