# -*- coding : utf-8 -*-
# @Time: 2024/1/29 21:02
# @Author: yefei.wang
# @File: demo.py

mod = 1000000007
mod2 = 998244353
y = 4
inv = pow(y, -1, mod2)

x1, x2 = 1, 3
z1 = x1 * inv
z2 = x2 * inv
print(z1, z2, z1 + z2)
