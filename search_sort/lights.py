import sys


def read_int_arr():
    return [int(x) for x in sys.stdin.readline().split(" ")]


x, n = read_int_arr()
pos = read_int_arr()
lights = [0] + sorted(pos) + [x]
l = len(lights)

adj = {lights[i]: [lights[i-1], lights[i+1]]
       for i in range(1, l - 1)}

adj[0] = [0, lights[1]]
adj[x] = [lights[l - 2], 0]

max_gap = max(lights[i+1] - lights[i] for i in range(l - 1))
best = [max_gap]

for p in pos[::-1]:
    left, right = adj.pop(p)
    max_gap = max(max_gap, right - left)
    adj[left][1] = right
    adj[right][0] = left
    best.append(max_gap)


print(*best[::-1][1:])
