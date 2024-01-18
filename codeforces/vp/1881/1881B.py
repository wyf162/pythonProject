import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')

tcn = I()
for _tcn_ in range(tcn):
    nums = LI()
    nums.sort()
    a, b, c = nums
    if a == b == c:
        YN(True)
    elif a == b and c == 2 * a:
        YN(True)
    elif a == b and c == 3 * a:
        YN(True)
    elif b == 2 * a and c == 2 * a:
        YN(True)
    elif b == a and c == 4 * a:
        YN(True)
    elif b == 2 * a and c == 3 * a:
        YN(True)
    else:
        YN(False)
