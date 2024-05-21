# -*- coding : utf-8 -*-
# @Time: 2024/5/19 20:18
# @Author: yefei.wang
# @File: F.py
# 容斥原理 组合数学


MOD = 10**9+7
n = int(input())
arr = list(map(int, input().split()))
s = sum(arr) % MOD
ans = s*(s-1)*(s-2)*(s-3)//12
ans -= sum(a*(a-1)*(a-2)//3 * (s-a) % MOD for a in arr)
ans -= sum(a*(a-1)*(a-2)*(a-3)//12 % MOD for a in arr)
ans += sum(a*(s-a)*(s-a-1) % MOD for a in arr)
print(ans % MOD)