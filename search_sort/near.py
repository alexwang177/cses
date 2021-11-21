import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

stack = []
ans = []

for i in range(n):

    while stack and arr[stack[len(stack) - 1]] >= arr[i]:
        stack.pop()

    if stack:
        ans.append(stack[len(stack) - 1] + 1)
    else:
        ans.append(0)

    stack.append(i)

print(*ans)
