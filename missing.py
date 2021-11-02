import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

a = 0
b = 0

for i in range(n):
    a ^= (i + 1)

    if i < len(arr):
        b ^= arr[i]

print(a ^ b)
