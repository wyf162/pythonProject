import sys

sys.stdin = open('../../input.txt', 'r')


def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def MI(): return map(int, input().split())
def GMI(): return map(lambda x: int(x) - 1, input().split())
def LI(): return list(MI())
def TI(): return tuple(MI())
def LGMI(): return list(GMI())
def YN(x): return print('YES' if x else 'NO')


mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k, m = MI()
    s = input()
    mask = 0
    for c in s:
        mask |= (1 << (ord(c) - ord('a')))
        if mask == (1 << k) - 1:
            
