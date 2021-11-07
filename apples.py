import sys


def gen_min_diff(arr, total, cur_sum, idx):

    if idx == len(arr):

        if total == cur_sum or cur_sum == 0:
            return float('inf')

        return abs((total - cur_sum) - cur_sum)

    min_diff = min(
        gen_min_diff(arr, total, cur_sum + arr[idx], idx + 1),
        gen_min_diff(arr, total, cur_sum, idx + 1)
    )

    return min_diff


n = int(sys.stdin.readline())
arr = list(int(x) for x in sys.stdin.readline().split(" "))

if n == 1:
    print(arr[0])
else:
    total = sum(arr)
    ans = gen_min_diff(arr, total, 0, 0)

    print(ans)
