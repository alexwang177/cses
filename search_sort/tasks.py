import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append([int(x) for x in sys.stdin.readline().split()])

arr.sort(key=lambda x: x[0])

cur_time = 0
reward = 0

for p in arr:
    cur_time += p[0]
    reward += p[1] - cur_time

print(reward)
