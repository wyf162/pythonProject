import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

N = 1000005
tree = [[] for _ in range(N)]
prev = [1]
i = 2
while i < N:
    curr = []
    for _ in range(len(prev) + 1):
        curr.append(i)
        i += 1
    for j in range(len(prev)):
        tree[prev[j]].append(curr[j])
        tree[prev[j]].append(curr[j + 1])
    prev = curr

ret = [0] * N

fa = [[] for _ in range(N)]
for i, xs in enumerate(tree):
    for x in xs:
        if x >= N:
            continue
        fa[x].append(i)
    ret[i] = i * i
    for j in fa[i]:
        ret[i] += ret[j]
    if len(fa[i]) == 2:
        i1, i2 = fa[i]
        for j in fa[i1]:
            if j in fa[i2]:
                ret[i] -= ret[j]

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    print(ret[n])
