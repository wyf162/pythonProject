# -*- coding : utf-8 -*-
# @Time: 2024/9/8 10:29
# @Author: yefei.wang
# @File: A.py

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(x))[2:] for x in date.split('-'))
