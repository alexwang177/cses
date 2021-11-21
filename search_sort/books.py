import sys

'''

4 6 7

1 2 3 4 5 6 7

7 + 1 + 2 + 3 + 4 >= 1 + 2 + 3 + 4 + 5

a) 7 7 7 7 7 7 7 4 4 4 4 6 6 6 6 6 6

b) 4 4 4 4 6 6 6 6 6 6 7 7 7 7 7 7 7

'''

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort()

print(max(sum(arr), 2*arr[n-1]))
