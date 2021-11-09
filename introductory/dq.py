import sys

'''
1-length starts at: 1

2-length starts at: 10

3-length starts at: 

x-length starts at: 1*9 + 2*90 + 3*900 + (x-1)*9*10^(x-2)

= k * 9 * 10 ^ (k-1) for k from 1 ... x-1

'''


def get_digit(target):

    idx = 1
    length = 1

    while idx + (length * 9 * 10**(length - 1)) < target:

        idx += (length * 9 * 10**(length - 1))
        length += 1

    num = 10**(length-1)

    # print(f"index: {idx}, length: {length}, target: {target}")

    blocks = (target - idx) // length
    offset = (target - idx) % length

    num += blocks

    # print(f"index: {idx}, length: {length}, target: {target}")

    return str(num)[offset]


q = int(sys.stdin.readline())

for _ in range(q):
    print(get_digit(int(sys.stdin.readline())))
