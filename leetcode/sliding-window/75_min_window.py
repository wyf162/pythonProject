# _*_ coding: utf-8 _*_
# @Time : 2022/3/26 下午7:28 
# @Author : wangyefei
# @File : 75_min_window.py
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_hst = dict(collections.Counter(t))
        print(target_hst)
        l, r = 0, 0
        ret = ""
        cur_hst = dict()
        while r < len(s):
            while self.check(target_hst, cur_hst) is False and r < len(s):
                cur_hst[s[r]] = 1 + cur_hst.get(s[r], 0)
                r += 1
            if self.check(target_hst, cur_hst):
                if not ret or len(ret) > r - l:
                    ret = s[l:r]
            while self.check(target_hst, cur_hst) is True and l < r:
                if not ret or len(ret) > r - l:
                    ret = s[l:r]
                cur_hst[s[l]] -= 1
                l += 1
        return ret

    @staticmethod
    def check(dict1, dict2):
        for k, v in dict1.items():
            if v <= dict2.get(k, 0):
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    ret = sol.minWindow(s, t)
    print(ret)
