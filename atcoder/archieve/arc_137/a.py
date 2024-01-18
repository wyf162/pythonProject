import sys
from math import gcd

if sys.platform.startswith('win'):
    sys.stdin = open('../everyday/input.txt', 'r')

l, r = list(map(int, input().split()))

K = 1500
for k in range(K):
    for i in range(k+1):
        j = k - i

        x = l + i
        y = r - j
        if gcd(x, y) == 1:
            print(y-x)
            exit(0)
