import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().strip().split(" ")]

print(len(set(arr)))
