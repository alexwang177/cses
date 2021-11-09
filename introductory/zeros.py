import sys

n = int(sys.stdin.readline())

ans = 0
f = 5

while n >= f:
    temp = n // f
    ans += temp
    f *= 5

print(ans)
