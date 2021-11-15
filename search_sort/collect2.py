import sys

'''
5 3
4 2 1 5 3
2 3
1 5
2 3

4 2 1 5 3  -> ans = 3

* 2 1

* 2 1

4 1 2 5 3  -> ans = 2


'''

n, m = [int(x) for x in sys.stdin.readline().split(" ")]
arr = [int(x) for x in sys.stdin.readline().split(" ")]

idx_map = {}

for i in range(n):
    idx_map[arr[i]] = i

ans = 1
check_set = set()

for x in range(1, n):
    if idx_map[x+1] < idx_map[x]:
        ans += 1


def add(i):
    if arr[i] > 1:
        check_set.add((arr[i] - 1, arr[i]))
    if arr[i] < n:
        check_set.add((arr[i], arr[i] + 1))


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    idx_map[arr[i]] = i
    idx_map[arr[j]] = j


for _ in range(m):

    a, b = [int(x) for x in sys.stdin.readline().split(" ")]
    a -= 1
    b -= 1
    add(a)
    add(b)

    for p in check_set:
        if idx_map[p[1]] < idx_map[p[0]]:
            ans -= 1

    swap(arr, a, b)

    for p in check_set:
        if idx_map[p[1]] < idx_map[p[0]]:
            ans += 1

    print(ans)
    check_set.clear()
