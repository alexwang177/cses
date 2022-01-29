import sys
from collections import deque


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def max_slide_window(arr, k, n):

    dq = deque([])
    ret = [0 for _ in range(n - k + 1)]
    p = 0
    ans = 0

    for i in range(n):

        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            ret[p] = arr[dq[0]]
            p += 1

        if p >= 1 and i - k >= 0 and i < n - 1:
            left = i - k
            right = i + 1
            m = arr[dq[0]]

            if arr[left] >= m and arr[right] >= m:
                # print(f"({left + 1}, {right + 1}) -> {m}")
                ans += (right - left + 1)

    return ans


n = int(sys.stdin.readline())
arr = ria()

ans = 2 * (n - 1)

for k in range(1, n-1):
    ans += max_slide_window(arr, k, n)

print(ans)
