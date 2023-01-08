# _*_ coding: utf-8 _*_
# @Time : 2022/12/25 12:05 PM 
# @Author : yefe
# @File : 6273_capture_forts

from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        empty, enemy, allay = None, None, None
        for i, fort in enumerate(forts):
            if fort == -1:
                if allay is not None and empty is not None and empty > allay:
                    allay = None
                empty = i
            elif fort == 1:
                if allay is not None and empty is not None and allay > empty:
                    empty = None
                allay = i

            if allay is not None and empty is not None:
                ans = max(ans, abs(allay - empty) - 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]
    forts = [1, 0, 0, -1, 0, 0, -1, 0, 0, 1]
    ret = sol.captureForts(forts)
    print(ret)
