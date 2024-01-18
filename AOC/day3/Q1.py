import sys

sys.stdin = open('./input.txt')

ans = 0
n = 140
ss = [input() for _ in range(n)]
for i in range(n):
    s = ss[i]
    j = 0
    while j < len(s):
        if s[j] == '.':
            j += 1
        elif '0' <= s[j] <= '9':
            k = 0
            isvalid = False
            while j < n and '0' <= s[j] <= '9':
                k *= 10
                k += (int(s[j]))
                for di in range(-1, 2, 1):
                    for dj in range(-1, 2, 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < len(s):
                            print(ni, nj)
                            if ss[ni][nj] != '.' and (ss[ni][nj] < '0' or ss[ni][nj] > '9'):
                                isvalid = True
                j += 1
            if isvalid:
                ans += k
        else:
            j += 1
print(ans)
