# _*_ coding: utf-8 _*_
# @Time : 2022/4/15 下午8:38 
# @Author : wangyefei
# @File : 385_deserialize.py
import json


class NestedInteger(object):
    def __init__(self, val=None):
        self.val = val if val else list()

    def add(self, elem):
        self.val.append(elem)


class Solution:
    def deserialize(self, s: str):
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, num, negative = [], 0, False
        for i, c in enumerate(s):
            if c == '-':
                negative = True
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(NestedInteger())
            elif c in ',]':
                if s[i - 1].isdigit():
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num, negative = 0, False
                if c == ']' and len(stack)>1:
                    stack[-2].add(stack.pop())
        return stack.pop()


if __name__ == '__main__':
    sol = Solution()
    s = "[123,[456,[789]]]"
    data = sol.deserialize(s)
    print(data)
    # data = json.loads(s)
    # print(data)
