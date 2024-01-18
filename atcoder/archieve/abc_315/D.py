from collections import deque

H, W = map(int, input().split())
row = [[0] * 26 for i in range(H)]
col = [[0] * 26 for i in range(W)]
for i in range(H):
    c = input()
    for j in range(W):
        row[i][ord(c[j]) - ord("a")] += 1
        col[j][ord(c[j]) - ord("a")] += 1
resr = set(range(H))
resc = set(range(W))
remove = deque()
ser = set()
for i in range(H):
    if row[i].count(0) == 25:
        remove.append((0, i))
        ser.add((0, i))
for i in range(W):
    if col[i].count(0) == 25:
        remove.append((1, i))
        ser.add((1, i))
while len(remove) > 0:
    t, p = remove.pop()
    if t == 0:
        pos = -1
        for i in range(26):
            if row[p][i] > 0:
                pos = i
                break
        if pos == -1:
            continue
        resr.discard(p)
        for i in resc:
            col[i][pos] -= 1
            if col[i].count(0) == 25:
                if sum(col[i]) > 1:
                    if (1, i) not in ser:
                        remove.append((1, i))
                        ser.add((1, i))
    else:
        pos = -1
        for i in range(26):
            if col[p][i] > 0:
                pos = i
        resc.discard(p)
        for i in resr:
            row[i][pos] -= 1
            if row[i].count(0) == 25:
                if sum(row[i]) > 1:
                    if (0, i) not in ser:
                        remove.append((0, i))
                        ser.add((0, i))
print(len(resr) * len(resc))
