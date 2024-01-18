import sys
from collections import defaultdict

sys.stdin = open('./input.txt')

gear = defaultdict(list)

ans = 0
n = 140
ss = [input() for _ in range(n)]
for i in range(n):
    s = ss[i]
    j = 0
    while j < n:
        if s[j] == '.':
            j += 1
        elif '0' <= s[j] <= '9':
            k = 0
            isvalid = False
            idxs = set()
            while j < n and '0' <= s[j] <= '9':
                k *= 10
                k += (int(s[j]))
                for di in range(-1, 2, 1):
                    for dj in range(-1, 2, 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            # print(ni, nj)
                            if ss[ni][nj] != '.' and (ss[ni][nj] < '0' or ss[ni][nj] > '9'):
                                isvalid = True
                            if ss[ni][nj] == '*':
                                idxs.add((ni, nj))
                j += 1
            if isvalid:
                for ni, nj in idxs:
                    gear[(ni, nj)].append(k)
        else:
            j += 1
for k, v in gear.items():
    if len(v) == 2:
        ans += v[0] * v[1]
print(ans)