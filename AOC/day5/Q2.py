import sys

sys.stdin = open('./input.txt', 'r')
nums = [17, 9, 40, 24, 20, 44, 41]
# sys.stdin = open('./i1.txt', 'r')
# nums = [2, 3, 4, 2, 3, 2, 2]

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

s = input()
seeds = [int(x) for x in s[7:].split()]
sections = []
for i in range(0, len(seeds), 2):
    left = seeds[i]
    right = seeds[i] + seeds[i + 1] - 1
    sections.append([left, right])

cvs = [[] for i in range(7)]
for i in range(7):
    input()
    input()
    cvs[i] = [LI() for _ in range(nums[i])]
    cvs[i].sort(key=lambda x: x[1])

rst = 10 ** 12
for section in sections:
    A = [section]
    for cv in cvs:
        res = []
        B = cv
        i, j = 0, 0
        while i < len(A) and j < len(B):
            a1, a2 = A[i]
            dest, src, rng = B[j]
            b1, b2 = src, src + rng - 1
            c = dest - src

            if b2 >= a1 and a2 >= b1:
                if a1 < b1 and a2 <= b2:
                    res.append([a1, b1 - 1])
                    res.append([b1 + c, a2 + c])
                elif a1 < b1 and a2 > b2:
                    res.append([a1, b1 - 1])
                    res.append([b1 + c, b2 + c])
                    A[i][0] = b2 + 1
                elif b1 <= a1 and a2 <= b2:
                    res.append([a1 + c, a2 + c])
                elif b1 <= a1 and b2 < a2:
                    res.append([a1 + c, b2 + c])
                    A[i][0] = b2 + 1
            elif a2 < b1:
                res.append([a1, a2])

            if b2 < a2:
                j += 1
            else:
                i += 1
        while i < len(A):
            a1, a2 = A[i]
            res.append([a1, a2])
            i += 1
        # print(res)
        A = res
        A.sort()
        print(A)
        print(sum(b - a + 1 for a, b in A))

    tmp = min(x[0] for x in A)
    rst = min(tmp, rst)
print(rst)
