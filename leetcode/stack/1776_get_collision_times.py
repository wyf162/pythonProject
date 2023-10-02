# _*_ coding: utf-8 _*_
# @Time : 2022/05/03 3:20 PM 
# @Author : yefe
# @File : 1776_get_collision_times
from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [0] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk:
                # 如果栈顶比我快，我追不上它，考虑等它消失后我去撞它前面的，所以pop
                if cars[stk[-1]][1] >= cars[i][1]:
                    stk.pop()
                else:
                    # 如果它不会消失，我肯定可以碰它
                    if ans[stk[-1]] < 0:
                        break
                    # 如果他会消失，我需要计算一下在消失前是否可以碰的上
                    d = ans[stk[-1]] * (cars[i][1] - cars[stk[-1]][1])
                    if d > cars[stk[-1]][0] - cars[i][0]:
                        break
                    else:
                        stk.pop()
            if not stk:
                ans[i] = -1
            else:
                t = (cars[stk[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stk[-1]][1])
                ans[i] = t
            stk.append(i)
        return ans


if __name__ == '__main__':
    sol = Solution()
    cars = [[1, 2], [2, 1], [4, 3], [7, 2]]
    ret = sol.getCollisionTimes(cars)
    print(ret)
