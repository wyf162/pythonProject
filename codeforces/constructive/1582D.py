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
    nums = LI()
    if n % 2 == 0:
        ans = []
        for i in range(0, n, 2):
            ans.append(nums[i + 1])
            ans.append(-nums[i])
        print(*ans)
    else:
        ans = []
        for i in range(0, n - 3, 2):
            ans.append(nums[i + 1])
            ans.append(-nums[i])
        a, b, c = nums[-3:]
        if a + b != 0:
            ans.extend([c, c, -(a + b)])
        elif a + c != 0:
            ans.extend([b, -(a + c), b])
        else:
            ans.extend([-(b + c), a, a])
        print(*ans)
