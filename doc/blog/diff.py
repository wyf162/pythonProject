# -*- coding: utf-8 -*-
# @Time: 2024/6/18 11:45
# @Author: yfwang
# @File: 差分.py


N = 5
d2 = [0] * (N + 2)
d = [0] * (N + 2)
f = [0] * (N + 2)
# 3 2 1 0 1
L1, R1, L2, R2 = 0, 4, 5, 4
f[L1] += R1 - L1
d2[L1] -= 1
d2[R1 + 1] += 1
d2[L2] += 1
d2[R2 + 1] -= 1

# L1, R1, L2, R2 = 0, 4, 4, 4
# # f[L1] += R1 - L1
# d2[L1] += 1
# d2[R1 + 1] -= 1
# d2[L2] += 1
# d2[R2 + 1] -= 1


for i in range(N):
    if i > 0:
        d[i] = d[i - 1] + d2[i]
    else:
        d[i] = d2[i]

for i in range(N):
    if i > 0:
        f[i] = f[i - 1] + d[i]
    else:
        continue

print(d)
print(f)
