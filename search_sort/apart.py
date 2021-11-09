import sys

'''

4 3 5
60 45 80 60
30 60 75

45 60 60 80

30 60 75

10 10 10
90 41 20 39 49 21 35 31 74 86
14 24 24 7 82 85 82 4 60 95

20 21 31 35 39 41 49 75 86 90
4  7  14 24 24 60 82 82 85 95

'''

n, m, k = [int(x) for x in sys.stdin.readline().strip().split(" ")]
app = [int(x) for x in sys.stdin.readline().strip().split(" ")]
apart = [int(x) for x in sys.stdin.readline().strip().split(" ")]

app.sort()
apart.sort()

i, j = 0, 0

ans = 0

while i < n and j < m:

    # apartment too small
    while i < n and j < m and apart[j] + k < app[i]:
        j += 1

    # app too small
    while i < n and j < m and app[i] + k < apart[j]:
        i += 1

    if i < n and j < m and abs(app[i] - apart[j]) <= k:
        ans += 1
        i += 1
        j += 1

print(ans)
