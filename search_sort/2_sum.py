import sys

n, x = [int(x) for x in sys.stdin.readline().split(" ")]
arr = [int(x) for x in sys.stdin.readline().split(" ")]

m = {}
found = False

for i in range(n):

    c = x - arr[i]

    if c in m:
        print(f"{m[c] + 1} {i + 1}")
        found = True
        break

    m[arr[i]] = i

if not found:
    print("IMPOSSIBLE")
