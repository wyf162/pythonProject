# -*- coding : utf-8 -*-
# @Time: 2024/7/7 10:20
# @Author: yefei.wang
# @File: A.py



class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        ans = []
        for i, c in enumerate(s):
            j = (i + k) % n
            ans.append(s[j])
        return ''.join(ans)
