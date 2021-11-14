import sys

'''
1 2 2 3 5
'''

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]
arr.sort()

idx = n // 2
ans = 0

for x in arr:
    ans += abs(x - arr[idx])

print(ans)
