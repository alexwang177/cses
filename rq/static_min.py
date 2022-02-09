import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


def gen_logs(n):
    log = [0 for _ in range(n+1)]
    log[1] = 0

    for i in range(2, n+1):
        log[i] = log[i//2] + 1

    return log


n, q = ria()
arr = ria()
log = gen_logs(n)
k = log[n] + 1

st = [[None for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    # range (i, i)
    st[i][0] = arr[i]

# try all lengths of ranges that are power of two (2^j)
for j in range(1, k+1):

    i = 0

    # iterate over all possible ranges of length 2^j
    while i + (1 << j) <= n:
        st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])
        i += 1

for _ in range(q):
    a, b = ria()
    a -= 1
    b -= 1

    j = log[b - a + 1]
    ans = min(st[a][j], st[b - (1 << j) + 1][j])
    print(ans)
