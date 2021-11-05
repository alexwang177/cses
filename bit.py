import sys

mod = 1000000007
n = int(sys.stdin.readline())

ans = 1

for _ in range(n):
    ans = (ans % mod * 2) % mod

print(ans)
