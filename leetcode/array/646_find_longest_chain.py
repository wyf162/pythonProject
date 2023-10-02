# _*_ coding: utf-8 _*_
# @Time : 2022/09/03 12:46 PM 
# @Author : yefe
# @File : 646_find_longest_chain

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()

        f = [0] * n
        for i in range(0, n):
            f[i] = 1
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)


if __name__ == '__main__':
    sol = Solution()
    pairs = [[1, 2], [2, 3], [3, 4]]
    ret = sol.findLongestChain(pairs)
    print(ret)
