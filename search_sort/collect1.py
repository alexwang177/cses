import sys

'''

1 2 3 5 4 6 8 7

try all pairs of numbers: x and x+1

if x comes before x+1, this is valid and the optimal strategy is to take x then x+1

if x comes after x+1, no matter what we cannot take x first. Thus, this will ALWAYS add 
an extra round. 

'''

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

idx_map = {}

for i in range(n):
    idx_map[arr[i]] = i

ans = 1

for x in range(1, n):
    if idx_map[x+1] < idx_map[x]:
        ans += 1

print(ans)
