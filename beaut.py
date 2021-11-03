import sys

# n = 5
# 1 3 5 2 4

# n = 7
# 1 3 5 7 2 4 6

# n = 8
# 1 3 5 7 2 4 6 8

n = int(sys.stdin.readline())

if n == 1:
    print(1)
elif n < 4:
    print("NO SOLUTION")
elif n == 4:
    print("2 4 1 3")
else:
    for i in range(1, n+1, 2):
        print(f"{i} ")

    for i in range(2, n+1, 2):
        print(f"{i} ")
