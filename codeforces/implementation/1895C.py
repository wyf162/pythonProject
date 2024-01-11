n = int(input())
A = [[int(c) for c in x] for x in input().split()]

precalc = [[[0] * (19 * a) for _ in range(a + 1)] for a in range(6)]
for num in A:
    a = len(num)
    precalc[a][0][s := sum(num)] += 1
    for i, c in enumerate(num):
        precalc[a][i + 1][s := s - 2 * c] += 1

luckies = 0
for a in range(1, 5 + 1):
    for b in range(1, 5 + 1):
        c = a + b
        if c & 1:
            continue
        mid1 = min(a, c // 2)
        mid2 = max(0, c // 2 - a)
        for s in range(-9 * min(a, b), 9 * min(a, b) + 1):
            luckies += precalc[a][mid1][s] * precalc[b][mid2][-s]

print(luckies)
