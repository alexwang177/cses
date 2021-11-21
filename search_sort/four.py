import sys

n, x = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]
pmap = {}
found = False

'''
if i = 3 and n = 5 that means we've already covered:

0 1
0 2
0 3
0 4

map: empty

1 2
1 3 
1 4

map: 1 0

2 3
2 4

map: 2 0, 2 1

3 4
'''

for i in range(n):

    for j in range(i+1, n):

        if found:
            break

        k = x - arr[i] - arr[j]

        if k in pmap:
            print(f"{i+1} {j+1} {pmap[k][0] + 1} {pmap[k][1] + 1}")
            found = True
            break

    # at this point, future pairs in the two loops above will never touch the range [0...i] again. So, add the pairs in [0...i] to the map.

    for j in range(0, i):
        pmap[arr[i] + arr[j]] = (i, j)


if not found:
    print("IMPOSSIBLE")
