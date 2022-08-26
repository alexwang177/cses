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
    def __init__(self, str, leaf_size=5):
        self.leaf_size = leaf_size
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

    def _inorder(self, node, leaf_vals):
        if not node:
            return

        self._inorder(node.left, leaf_vals)
        
        print(f'{node}\n')

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


raw_str = "Hello_my_name_is_Simon"
rope = Rope(raw_str)
print(rope.get_str())

for i in range(len(raw_str)):
    print(rope.index(i))
