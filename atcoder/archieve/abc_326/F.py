import sys
from typing import List
from collections import Counter

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

N, X, Y = MI()
A = LI()

xs = []
ys = []
for i in range(N):
    if i % 2 == 1:
        xs.append(A[i])
    else:
        ys.append(A[i])


def solve(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    mid = n // 2
    hst1 = dict()
    hst1[0] = 0
    for i in range(mid):
        tmp = dict()
        for k, v in hst1.items():
            if nums[i] + k not in hst1:
                tmp[nums[i] + k] = nums[i]
        for k, v in tmp.items():
            hst1[k] = v

    hst2 = dict()
    hst2[0] = 0
    for i in range(mid, n):
        tmp = dict()
        for k, v in hst2.items():
            if nums[i] + k not in hst2:
                tmp[nums[i] + k] = nums[i]
        for k, v in tmp.items():
            hst2[k] = v

    ks1 = sorted(hst1.keys())
    ks2 = sorted(hst2.keys())
    l = len(ks1) - 1
    r = 0
    while l >= 0 and r < len(ks2):
        if ks1[l] + ks2[r] == target:
            break
        elif ks1[l] + ks2[r] < target:
            r += 1
        else:
            l -= 1

    if l < 0 or r >= len(ks2):
        return []
    else:
        lv = ks1[l]
        rst = []
        while lv > 0:
            rst.append(hst1[lv])
            lv -= hst1[lv]
        rv = ks2[r]
        while rv > 0:
            rst.append(hst2[rv])
            rv -= hst2[rv]
        cnt = Counter(rst)
        res = [0] * n
        for i in range(n):
            if cnt[nums[i]] > 0:
                res[i] = 1
                cnt[nums[i]] -= 1
        return res


s_x = sum(xs)
if (s_x + X) % 2:
    exit(print('No'))
target_x = (s_x + X) // 2

ret1 = solve(xs, target_x)
if not ret1:
    exit(print('No'))

s_y = sum(ys)
if (s_y + Y) % 2:
    exit(print('No'))
target_y = (s_y + Y) // 2
ret2 = solve(ys, target_y)
if not ret2:
    exit(print('No'))

# up, down, left, right
ans = []
i = 0
current_direction = 'left'
while i < len(ret2):
    if ret2[i] == 1:
        if current_direction == 'left':
            ans.append('L')
        else:
            ans.append('R')
        current_direction = 'up'
    else:
        if current_direction == 'left':
            ans.append('R')
        else:
            ans.append('L')
        current_direction = 'down'

    if i < len(ret1):
        if ret1[i] == 1:
            if current_direction == 'down':
                ans.append('L')
            else:
                ans.append('R')
            current_direction = 'left'
        else:
            if current_direction == 'up':
                ans.append('L')
            else:
                ans.append('R')
            current_direction = 'right'
    i += 1
print('Yes')
print(''.join(ans))

