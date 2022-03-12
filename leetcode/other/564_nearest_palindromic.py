# _*_ coding: utf-8 _*_
# @Time : 2022/3/2 下午9:28 
# @Author : wangyefei
# @File : 564_nearest_palindromic.py

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # if n == '10' or n == '11':
        #     return '9'
        if len(n) <= 1:
            return str(int(n) - 1)
        ans = list()
        nums = list(n)
        l = len(nums)
        if l & 1:
            m = l >> 1
            x = int("".join(nums[:m + 1]))
            for d_x in [-1, 0, 1]:
                left_x = x + d_x
                left_x = list(str(left_x))
                if len(left_x) == m + 2:
                    left_x = "1" + "0" * (l - 1) + "1"
                elif len(left_x) == m:
                    left_x = "9" * (l - 1)
                else:
                    left_x = left_x + list(reversed(left_x[:-1]))
                ans.append(int("".join(left_x)))
        else:
            m = l >> 1
            x = int("".join(nums[:m]))
            for d_x in [-1, 0, 1]:
                left_x = x + d_x
                left_x = list(str(left_x))
                if len(left_x) == m - 1 or left_x == ['0']:
                    left_x = "9" * (l - 1)
                elif len(left_x) == m + 1:
                    left_x = "1" + "0" * (l - 1) + "1"
                else:
                    left_x = left_x + list(reversed(left_x[:]))
                ans.append(int("".join(left_x)))
        print(ans)
        ret = ans[0]
        n = int(n)
        tmp = abs(ans[0] - n)
        for i in range(1, 3):
            if tmp > abs(ans[i] - n) > 0:
                tmp = abs(ans[i] - n)
                ret = ans[i]
        return str(ret)


if __name__ == '__main__':
    sol = Solution()
    n = "100"
    res = sol.nearestPalindromic(n)
    print(res)
