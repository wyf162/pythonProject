import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
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
    n = I()
    a = LI()
    groups = [[]]
    for i in range(n):
        if a[i] == 0:
            groups.append([])
        else:
            groups[-1].append((a[i], i))


    def func(nums):
        neg = two = 0
        mx = l = r = 0
        for _, t in enumerate(nums):
            num, j = t
            if num < 0: neg += 1
            if num in [-2, 2]: two += 1
            if neg % 2 == 0:
                if two > mx:
                    mx, l, r = two, nums[0][1], j

        neg = two = 0
        for _, t in enumerate(nums[::-1]):
            num, j = t
            if num < 0: neg += 1
            if num in [-2, 2]: two += 1
            if neg % 2 == 0:
                if two > mx:
                    mx, l, r = two, j, nums[-1][1]
        return mx, l, r


    rst, left, right = 0, n, 0
    for group in groups:
        mx, l, r = func(group)
        if mx > rst:
            rst = mx
            left = l
            right = n - r - 1
    print(left, right)
