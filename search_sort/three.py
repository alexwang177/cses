import sys

n, x = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]
arr = [(arr[i], i+1) for i in range(n)]
arr.sort()
found = False

for i in range(n):
    a = arr[i]

    j = i + 1
    k = n - 1

    while j < k:
        cur_sum = arr[i][0] + arr[j][0] + arr[k][0]

        if cur_sum > x:
            k -= 1
        elif cur_sum < x:
            j += 1
        else:
            print(f"{arr[i][1]} {arr[j][1]} {arr[k][1]}")
            found = True
            break

if not found:
    print("IMPOSSIBLE")
