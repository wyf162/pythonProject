import sys

sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../jury.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
queries = [LI() for _ in range(n)]


def solve(l, r):
    x = l
    for y in range(l, r + 1):
        if bin(y).count('1') > bin(x).count('1'):
            x = y
    print(x)


for l, r in queries:
    solve(l, r)
