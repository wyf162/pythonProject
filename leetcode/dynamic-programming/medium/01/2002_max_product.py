# _*_ coding: utf-8 _*_
# @Time : 2022/10/15 9:34 PM 
# @Author : yefe
# @File : 2002_max_product


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palins = []  # 哈希表，保存所有的回文数字
        for num in range(1, 2**n):
            arr = []
            for j in range(n):
                if num & (1 << j):
                    arr.append(s[j])
            # 检查数字映射的序列是否为回文序列，如果是，将其加入数组
            isPalin = True
            for j in range(len(arr) // 2):
                if arr[j] != arr[-j - 1]:
                    isPalin = False
                    break
            if isPalin:
                palins.append(num)
        # 下面开始找到长度乘积最大的不相交回文串
        ans = 0
        for i in range(len(palins)):
            for j in range(i + 1, len(palins)):
                if palins[i] & palins[j] == 0:
                    ans = max(ans, palins[i].bit_count() * palins[j].bit_count())
        return ans


