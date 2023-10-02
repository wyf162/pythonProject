# -*- coding : utf-8 -*-
# @Time: 2022/7/13 20:35
# @Author: yefei.wang
# @File: 735_asteroid_collision.py
from typing import List


class Solution:
    @staticmethod
    def asteroid_collision(asteroids: List[int]) -> List[int]:
        right = []
        for asteroid in asteroids:
            if asteroid > 0 or not right:
                right.append(asteroid)
            elif asteroid < 0:
                if right[-1] < 0:
                    right.append(asteroid)
                else:
                    if right[-1] < abs(asteroid):
                        right[-1] = asteroid
                    elif right[-1] > abs(asteroid):
                        continue
                    else:
                        right.pop()

        left = []
        for asteroid in reversed(right):
            if asteroid < 0 or not left:
                left.append(asteroid)
            elif asteroid > 0:
                if left[-1] > 0:
                    left.append(asteroid)
                elif left[-1] < 0:
                    if abs(left[-1]) < asteroid:
                        left[-1] = asteroid
                    elif abs(left[-1]) > asteroid:
                        continue
                    else:
                        left.pop()

        return left[::-1]

    @staticmethod
    def isValid(result):
        if not result:
            return True
        n = len(result)
        i = 0
        while i < n:
            if result[i] > 0:
                break
            i += 1
        while i < n:
            if result[i] < 0:
                return False
            i += 1
        return True

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = self.asteroid_collision(asteroids)
        while not self.isValid(ret):
            ret = self.asteroid_collision(ret)
        return ret


if __name__ == '__main__':
    sol = Solution()
    # asteroids = [5, 10, -5]
    # asteroids = [8, -8]
    # asteroids = [10, 2, -5]
    # asteroids = [-2, -1, 1, 2]
    asteroids = [7, -1, 2, -3, -6, -6, -6, 4, 10, 2]
    ret = sol.asteroidCollision(asteroids)
    print(ret)
