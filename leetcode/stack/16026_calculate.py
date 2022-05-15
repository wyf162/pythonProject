# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 7:02 PM 
# @Author : yefe
# @File : 16026_calculate
class Solution:
    def calculate(self, s: str) -> int:
        signs = []
        nums = []
        i = 0
        n = len(s)
        while i<n:
            if s[i].isdigit():
                num = int(s[i])
                i += 1
                while i<n and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
                nums.append(num)
                if signs and signs[-1] in '*/':
                    num1=nums.pop()
                    num2=nums.pop()
                    sign = signs.pop()
                    if sign=='*':
                        nums.append(num1*num2)
                    elif sign=='/':
                        nums.append(int(num2/num1))
            elif s[i] in '+-*/':
                signs.append(s[i])
                i += 1
            else:
                i += 1
        for i, sign in enumerate(signs):
            if sign=='+':
                nums[i+1] = nums[i]+nums[i+1]
            elif sign=='-':
                nums[i + 1] = nums[i] - nums[i + 1]
        return nums[-1]


if __name__ == '__main__':
    sol = Solution()
    # s = "3+2*2 "
    s = "1-1+1"
    ret = sol.calculate(s)
    print(ret)

