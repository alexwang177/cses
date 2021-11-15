import sys
import bisect

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

towers = []

for x in arr:
    i = bisect.bisect_right(towers, x)
    # print(f"insert {x} at idx {i}")

    if i == len(towers):
        towers.append(x)
    else:
        towers[i] = x

    # print(towers)

print(len(towers))
