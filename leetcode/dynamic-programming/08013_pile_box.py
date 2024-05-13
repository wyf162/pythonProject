# _*_ coding: utf-8 _*_
# @Time : 2022/05/20 10:00 PM 
# @Author : yefe
# @File : 08013_pile_box
from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        n = len(box)
        box.sort()
        dp = [0]*n
        for i in range(n):
            for j in range(i):
                if box[i][0]>box[j][0] and box[i][1]>box[j][1] and box[i][2]>box[j][2]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += box[i][2]
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    ret = sol.pileBox(box)
    print(ret)
