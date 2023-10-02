# -*- coding : utf-8 -*-
# @Time: 2022/7/1 19:54
# @Author: yefei.wang
# @File: 241_diff_way_to_compute.py
from typing import List


def compute(op, num1, num2):
    if op=='-':
        return num1-num2
    elif op=='+':
        return num1+num2
    elif op=='*':
        return num1*num2


class Solution:
    def diffWaysToCompute2(self, expression: str) -> List[int]:

        nums = []
        ops = []
        i = 0
        n = len(expression)
        while i<n:
            if expression[i].isdigit():
                num = 0
                while i<n and expression[i].isdigit():
                    num = num*10+int(expression[i])
                    i += 1
                nums.append(num)
            else:
                ops.append(expression[i])
                i += 1
        print(nums)
        print(ops)
        rets = []

        def dfs(nums,ops):
            if len(ops)==0:
                rets.append(nums[0])
            else:
                for i in range(len(ops)):
                    dfs(nums[:i]+[compute(ops[i], nums[i], nums[i+1])]+nums[i+2:],
                        ops[:i]+ops[i+1:])

        dfs(nums, ops)

        return rets

    def diffWaysToCompute(self, expression: str) -> List[int]:

        nums = []
        ops = []
        i = 0
        n = len(expression)
        while i<n:
            if expression[i].isdigit():
                num = 0
                while i<n and expression[i].isdigit():
                    num = num*10+int(expression[i])
                    i += 1
                nums.append(num)
            else:
                ops.append(expression[i])
                i += 1
        print(nums)
        print(ops)
        rets = []

        def dfs(nums,ops):
            if len(ops)==0:
                rets.append(nums[0])
            else:
                for i in range(len(ops)):
                    dfs(nums[:i]+[compute(ops[i], nums[i], nums[i+1])]+nums[i+2:],
                        ops[:i]+ops[i+1:])

        dfs(nums, ops)

        return rets


if __name__ == '__main__':
    sol = Solution()
    expression = "2-1-1"
    rets = sol.diffWaysToCompute(expression)
    print(rets)