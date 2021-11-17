import sys
import functools

'''
4
1 6
2 4
4 8
3 6

1 -> 0
2 -> 1
3 -> 2
4 -> 3
6 -> 4
8 -> 5

0 4
1 3
3 5
2 4

0 1 2 3 4 5
- - - - - 
  - - -
      - - -
    - - -

'''


def customsort1(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]

    return a[0] - b[0]


n = int(sys.stdin.readline())
arr = []

for i in range(n):
    l, r = [int(x) for x in sys.stdin.readline().split(" ")]
    arr.append((l, r, i))

ans = [0] * n
arr1 = sorted(arr, key=functools.cmp_to_key(customsort1))

min_end = float('inf')

for i in range(n-1, -1, -1):
    if min_end <= arr1[i][1]:
        ans[arr1[i][2]] = 1
    else:
        ans[arr1[i][2]] = 0

    min_end = min(min_end, arr1[i][1])

print(*ans)

max_end = 0

for i in range(n):
    if max_end >= arr1[i][1]:
        ans[arr1[i][2]] = 1
    else:
        ans[arr1[i][2]] = 0

    max_end = max(max_end, arr1[i][1])

print(*ans)

min_end = float('inf')
