import sys

s = list(sys.stdin.readline().strip())
#s = list("CCA")

ch_dict = {}

for c in s:
    if c in ch_dict:
        ch_dict[c] += 1
    else:
        ch_dict[c] = 1

ch_odd = None
valid = True

for c, f in ch_dict.items():
    if f % 2 == 1:
        if ch_odd:
            valid = False
            print("NO SOLUTION")
            break

        ch_odd = c

if valid:

    left = 0
    right = len(s) - 1

    for c, f in ch_dict.items():
        if c == ch_odd:
            continue

        while f > 0:
            s[left] = c
            s[right] = c
            left += 1
            right -= 1
            f -= 2

    if ch_odd:

        while left <= right:
            s[left] = ch_odd
            left += 1

    print(''.join(s))
