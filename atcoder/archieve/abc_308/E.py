import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353


def get_mex(nums):
    nums.sort()
    mex = 0
    for num in nums:
        if num == mex:
            mex += 1
    return mex


n = I()
a = LI()
s = input()

# mtx = {
#     'M0': 0, 'M1': 0, 'M2': 0,
#     'E0': 0, 'E1': 0, 'E2': 0,
#     'X0': 0, 'X1': 0, 'X2': 0,
# }
mtx = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

m = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    for j in range(3):
        if a[i] == j and s[i] == 'M':
            m[i][j] = m[i - 1][j] + 1
        else:
            m[i][j] = m[i - 1][j]

x = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    for j in range(3):
        if s[n - 1 - i] == 'X' and a[n - 1 - i] == j:
            x[i][j] = x[i - 1][j] + 1
        else:
            x[i][j] = x[i - 1][j]

rst = 0
for i in range(n):
    if s[i] == 'E':
        for j in range(3):
            for k in range(3):
                mex = get_mex([j, k, a[i]])
                rst += m[i][j] * x[n - 1 - i][k] * mex
print(rst)
