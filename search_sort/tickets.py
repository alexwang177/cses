import sys
from bisect import bisect_right

'''
5 3
5 3 7 8 5
4 8 3

3 5 5 7 8
'''


n, m = [int(x) for x in sys.stdin.readline().split(" ")]
ticket = [int(x) for x in sys.stdin.readline().split(" ")]
cust = [int(x) for x in sys.stdin.readline().split(" ")]

ticket.sort()
