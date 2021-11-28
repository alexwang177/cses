import sys

'''
5 2
1 2 3 1 1

1
1 2
2
2 3
3
3 1
3 1 1
1
1 1
1

'''

n, k = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]

freq = {}
ans = 0
r = 0

for l in range(n):

    # arr[r] has not been looked at yet

    while r < n and (len(freq) < k or (len(freq) == k and arr[r] in freq)):
        if arr[r] not in freq:
            freq[arr[r]] = 0

        freq[arr[r]] += 1
        r += 1

    # the window should contain k elements or less at this point

    ans += (r - l)
    # print(f"{l} -> {r}")
    freq[arr[l]] -= 1

    if freq[arr[l]] == 0:
        freq.pop(arr[l])

print(ans)
