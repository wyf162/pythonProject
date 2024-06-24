import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
B = 2

l, r = MI()

if l == r:
    exit(print(0))
for i in range(60, -1, -1):
    if l >> i != r >> i:
        exit(print((1 << i + 1) - 1))
