import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]
arr.sort()

'''
5
2 9 1 2 7

1 2 2 7 9

cur: 3
'''

cur_sum = 0

for i in range(n):
    if cur_sum + 1 < arr[i]:
        break
    else:
        cur_sum += arr[i]

print(cur_sum + 1)
