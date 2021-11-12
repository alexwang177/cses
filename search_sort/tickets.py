import sys

'''
5 3
5 3 7 8 5
4 8 3

3 5 5 7 8
'''

from bst import BST


# n, m = [int(x) for x in sys.stdin.readline().split(" ")]
# ticket = [int(x) for x in sys.stdin.readline().split(" ")]
# cust = [int(x) for x in sys.stdin.readline().split(" ")]

ticket = [-1, 99, 0, 2, 5, 0, 13, 2, 8]

tree = BST()

for t in ticket:
    tree.add(t)

# for c in cust:
#     t = tree.find_ticket(c)

#     if t:
#         print(t)
#         tree.remove(t)
#     else:
#         print(-1)

tree.print_tree()
