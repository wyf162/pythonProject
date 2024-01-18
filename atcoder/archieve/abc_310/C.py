import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
stick_list = set()
stick_num = 0
for i in range(n):
    before_num = len(stick_list)
    s = input()
    stick_list.add(s)
    stick_list.add(s[::-1])
    after_num = len(stick_list)
    if before_num != after_num:
        stick_num += 1
print(stick_num)
