import sys

'''
    n = 1

    0
    1

    n = 2

    00
    01
    11
    10

    n = 3
    
    000
    001
    011
    010

    110
    111
    101
    100

'''


def gen_gray_code(k):

    if k == 1:
        return ["0", "1"]

    prev_gc = gen_gray_code(k - 1)
    gc = []

    for b in prev_gc:
        gc.append("0" + b)

    for b in reversed(prev_gc):
        gc.append("1" + b)

    return gc


n = int(sys.stdin.readline())

gray_code = gen_gray_code(n)

for b in gray_code:
    print(b)
