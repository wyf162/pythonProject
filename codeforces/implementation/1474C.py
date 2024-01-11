import sys
from collections import Counter

sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

YES = 'Yes'
NO = 'No'

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
