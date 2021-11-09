import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

moves = 0

for i in range(1, n):
    prev = arr[i-1]

    if prev > arr[i]:
        moves += prev - arr[i]
        arr[i] = prev

print(moves)
