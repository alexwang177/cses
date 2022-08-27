def printTree(root, markerStr="+- ", levelMarkers=[]):
    emptyStr = " "*len(markerStr)
    connectionStr = "|" + emptyStr[:-1]
    level = len(levelMarkers)
    mapper = lambda draw: connectionStr if draw else emptyStr
    markers = "".join(map(mapper, levelMarkers[:-1]))
    markers += markerStr if level > 0 else ""
    print(f"{markers}{root}")

    children = []

    if root.left is not None:
        children.append(root.left)
    if root.right is not None:
        children.append(root.right)

    for i, child in enumerate(children):
        isLast = i == len(children) - 1
        printTree(child, markerStr, [*levelMarkers, not isLast])

class RopeNode:
    def __init__(self, val, left, right):
        self.left = left
        self.right = right
        self.val = val

        self.weight = 0
        self.length = 0

        if self.val is not None:
            self.weight = len(self.val)
            self.length = len(self.val)
        else:

            self.weight = 0
            self.length = 0
            
            if self.left is not None:
                self.weight += left.length
                self.length += left.length

            if self.right is not None:
                self.length += right.length

    def __repr__(self):
        return f'val: {self.val} weight: {self.weight}'
    
class Rope:
    def __init__(self, str=None, root=None, leaf_size=5):
        self.leaf_size = leaf_size

        if root is not None:
            self.root = root
        else:
            self.root = self._build_tree(str, 0, len(str))

    def _build_tree(self, str, lo, hi):
        
        length = hi - lo

        if length <= self.leaf_size:
            leaf = RopeNode(str[lo:hi], None, None)
            return leaf

        mid = lo + (hi - lo) // 2
        left_node = self._build_tree(str, lo, mid)
        right_node = self._build_tree(str, mid, hi)

        return RopeNode(None, left_node, right_node)

    def _inorder_print(self, node):
        if not node:
            return

        self._inorder_print(node.left)
        print(f'{node}\n')
        self._inorder_print(node.right)

    def _inorder(self, node, leaf_vals):
        if not node:
            return

        self._inorder(node.left, leaf_vals)
        
        if node.val is not None:
            leaf_vals.append(node.val)

        self._inorder(node.right, leaf_vals)

    def get_str(self):
        leaf_vals = []
        self._inorder(self.root, leaf_vals)
        return ''.join(leaf_vals)

    def index(self, i):
        return self._index(self.root, i+1)
    
    def _index(self, node, i):

        if i > node.weight:
            return self._index(node.right, i - node.weight)

        if i <= node.weight and node.val is not None:
            return node.val[i-1]
        
        return self._index(node.left, i)

    def _concat(self, node_1, node_2):
        return RopeNode(None, node_1, node_2)

    def _split_leaf(self, leaf, i):
        leaf_left = RopeNode(leaf.val[:i], None, None)
        leaf_right = RopeNode(leaf.val[i:], None, None)
        return (leaf_left, leaf_right)

    def _split(self, node, i):


        # i is in middle of leaf node's val
        if i < node.weight and node.val is not None:
            return self._split_leaf(node, i)

        if i < node.weight:
            lhs, rhs = self._split(node.left, i)
            return (lhs, self._concat(rhs, node.right))
        elif i > node.weight:
            lhs, rhs = self._split(node.right, i - node.weight)
            return (self._concat(node.left, lhs), rhs)
        else:
            return (node.left, node.right)

    def append(self, new_str):
        new_rope = Rope(new_str)
        return Rope(root=self._concat(self.root, new_rope.root))

    def prepend(self, new_str):
        new_rope = Rope(new_str)
        return Rope(root=self._concat(new_rope.root, self.root))

    def insert(self, new_str, i):

        if i < 0 or i >= self.root.length:
            raise Exception('Invalid index')

        if i == 0:
            return self.prepend(new_str)

        if i == self.root.length:
            return self.append(new_str)

        lhs, rhs = self._split(self.root, i)
        new_rope = Rope(new_str)

        return Rope(root=self._concat(self._concat(lhs, new_rope.root), rhs))

raw_str = "Hello_my_name_is_Simon"
rope = Rope(raw_str)

printTree(rope.root)
print(rope.get_str())

print('--------------------------------------\n')

node_left, node_right = rope._split(rope.root, 7)
printTree(node_left)

print('--------------------------------------\n')

printTree(node_right)

print('--------------------------------------\n')

rope = rope.append("And_my_name_is_Alex!")
rope = rope.prepend("This_is_the_beginning_____")
printTree(rope.root)
print(rope.get_str())

print('--------------------------------------\n')

rope = rope.insert("xxxxxxxxxxxxxxxxxxxx", 45)
printTree(rope.root)
print(rope.get_str())





