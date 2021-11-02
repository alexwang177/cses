import sys

num = int(sys.stdin.readline())

while num > 1:

    print(f"{num} ")

    if num % 2 == 0:
        num = num // 2
    else:
        num = 3*num + 1

print(num)
