import sys


def gen_strs(gen, s, used, build):

    if len(build) == len(s):
        gen.append(build)
        return

    for i in range(len(s)):

        if i in used or (i > 0 and s[i] == s[i-1] and i-1 not in used):
            continue

        used.add(i)
        gen_strs(gen, s, used, build + s[i])
        used.remove(i)


s = list(sys.stdin.readline().strip())
s.sort()

gen = []
gen_strs(gen, s, set(), "")

print(len(gen))

for s in gen:
    print(s)
