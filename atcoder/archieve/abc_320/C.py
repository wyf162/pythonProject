import itertools
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

M = I()
s1 = input()
s2 = input()
s3 = input()
ans = 3 * M + 1


def solve(t1, t2, t3):
    for i in range(M):
        for j in range(i + 1, 2 * M):
            for k in range(j + 1, 3 * M):
                if t1[i] == t2[j] == t3[k]:
                    global ans
                    ans = min(ans, k)


for ss in itertools.permutations([s1, s2, s3]):
    solve(ss[0], ss[1] * 2, ss[2] * 3)

print(ans if ans <= 3 * M else -1)
