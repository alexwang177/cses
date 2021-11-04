import sys

n = int(sys.stdin.readline())

total = (n * (n + 1)) // 2

if total % 2 == 0:

    print("YES\n")

    half = total // 2

    target = half
    first_set = set()

    for i in range(n, 0, -1):
        if i <= target:
            first_set.add(i)
            target -= i

    first_str = ' '.join(str(x) for x in sorted(list(first_set)))
    print(f"{len(first_set)}\n")
    print(f"{first_str}\n")

    print(f"{n - len(first_set)}\n")

    for i in range(1, n+1):
        if i not in first_set:
            print(f"{i} ")

else:
    print("NO")
