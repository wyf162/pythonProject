import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    A = LI()

    nums = [1]
    c = 1
    for i in range(2, n):
        if A[i] > A[i - 1]:
            c += 1
        else:
            nums.append(c)
            c = 1
    nums.append(c)
    print(nums)
    d = -1
    i1 = 0
    il = 1
    while i1 < len(nums):
        d += 1
        i1, il = i1 + il, sum(nums[i1:i1 + il])
    print(d)
