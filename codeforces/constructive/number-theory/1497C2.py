import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    ans = [1] * (k - 3)
    n = n - (k - 3)
    if n % 2 == 1:
        ans.extend([1, n // 2, n // 2])
    elif n % 4 == 0:
        ans.extend([n // 2, n // 4, n // 4])
    else:
        ans.extend([2, n // 2 - 1, n // 2 - 1])
    print(*ans)
