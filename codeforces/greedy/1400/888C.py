import sys

sys.stdin = open('../../input.txt')
s = input()
n = len(s)
g = [[] for _ in range(26)]
for i, c in enumerate(s):
    k = ord(c) - ord('a')
    g[k].append(i)

ans = n
for k in range(26):
    if not g[k]:
        continue
    t = 0
    for i, c in enumerate(g[k]):
        if i == 0:
            t = max(t, c + 1)
        else:
            t = max(t, c - g[k][i - 1])
    t = max(t, n - g[k][-1])

    ans = min(ans, t)
print(ans)
