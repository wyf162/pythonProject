import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N = I()
A = LI()
S = input()

pre_sum = [0] * N
for i in range(N - 1):
    pre_sum[i + 1] = pre_sum[i] + int(S[i] == '1')

for i in range(N):
    j = A[i] - 1
    if i > j:
        i, j = j, i
    if pre_sum[j] - pre_sum[i] == (j - i):
        continue
    else:
        exit(print('NO'))
print('YES')
