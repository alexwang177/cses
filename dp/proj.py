import sys


def ria():
    return [int(x) for x in sys.stdin.readline().split()]


n = int(sys.stdin.readline())
projects = []
times = set()

for _ in range(n):
    projects.append(ria())
    times.add(projects[-1][0])
    times.add(projects[-1][1])

times = sorted(list(times))
compressed = {times[i]: i+1 for i in range(len(times))}

end_to_projects = {}

for p in projects:

    end_time = compressed[p[1]]

    if end_time not in end_to_projects:
        end_to_projects[end_time] = []

    end_to_projects[end_time].append(p)

dp = [0 for _ in range(len(times) + 1)]

for i in range(1, len(times) + 1):

    dp[i] = dp[i-1]

    if i in end_to_projects:
        for p in end_to_projects[i]:
            dp[i] = max(dp[i], dp[compressed[p[0]] - 1] + p[2])

print(dp[len(times)])

'''

do coordinate compression (this requires sorting)

dp[i] = max reward through day i

dp[i] = max (

    dp[i-1] -> no reward collected on day i

    dp[p.start - 1] + p.reward -> reward collected on day i from project p

)

'''
