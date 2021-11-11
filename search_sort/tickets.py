import sys

'''
5 3
5 3 7 8 5
4 8 3

3 5 5 7 8
'''


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

    def find_min(node):
        while node.left:
            node = node.left

        return node

    def print_inorder(self, node):

        if node == None:
            return

        self.print_inorder(node.left)
        print(node.data, sep="")
        self.print_inorder(node.right)

    def print_tree(self):
        self.print_inorder(self.root)


# n, m = [int(x) for x in sys.stdin.readline().split(" ")]
# ticket = [int(x) for x in sys.stdin.readline().split(" ")]
# cust = [int(x) for x in sys.stdin.readline().split(" ")]

ticket = [1, 23, 8, 7, 5, 99, 0, 7, 7, 14]

tree = BST()

for t in ticket:
    tree.add(t)

tree.print_tree()

print("--------------------")

tree.remove(99)
tree.remove(7)
tree.remove(7)
tree.remove(0)

tree.print_tree()
