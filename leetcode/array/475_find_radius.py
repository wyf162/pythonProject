# -*- coding : utf-8 -*-
# @Time: 2021/12/20 22:12
# @Author: yefei.wang
# @File: 475_find_radius.py
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n,m = len(houses), len(heaters)
        i,j=0,0
        ans = 0
        while i<n:
            if houses[i]<=heaters[j]:
                ans = max(ans, heaters[j]-houses[i])
                i = i+1
            else:
                if j+1<m:
                    print(abs(houses[i]-heaters[j]) , abs(houses[i]-heaters[j+1]))
                    if abs(houses[i]-heaters[j]) < abs(houses[i]-heaters[j+1]):
                        ans = max(ans, abs(houses[i]-heaters[j]))
                        i = i+1
                    else:
                        j = min(j+1, m-1)
                else:
                    ans = max(ans,abs(houses[i]-heaters[j]))
                    i = i+1
        return ans


if __name__ == "__main__":
    sol=Solution()
    houses = [282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923]
    heaters = [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612]
    # 161834419
    houses = [1, 2, 3, 5, 15]
    heaters = [2, 30]
    print(sol.findRadius(houses,heaters))