import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


n = int(sys.stdin.readline())
prev = None
head = None

for i in range(1, n+1):
    node = Node(i)

    if not head:
        head = node

    if prev:
        prev.next = node

    prev = node

# make circular
node.next = head
size = n

prev = node
node = head
k = 1

'''

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

p    n                

     3 ->      5 ->     7  

     p          n

'''

while size > 1:

    prev = node
    node = node.next
    k += 1

    if k == 2:

        print(node.val)

        prev.next = node.next
        size -= 1
        k = 0

node = node.next
print(node.val)
