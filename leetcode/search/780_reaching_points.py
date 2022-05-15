# _*_ coding: utf-8 _*_
# @Time : 2022/4/9 下午12:47 
# @Author : wangyefei
# @File : 780_reaching_points.py
import collections


class Solution:
    def reachingPoints2(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        q = collections.deque()
        q.append((sx,sy))
        while q:
            cx,cy = q.popleft()
            if cx==tx and cy==ty:
                return True
            nx, ny = cx+cy, cy
            if nx<=tx and ny<=ty:
                q.append((nx,ny))
            nx, ny = cx, cx+cy
            if nx<=tx and ny<=ty:
                q.append((nx, ny))

        return False

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    sx = 1
    sy = 1
    tx = 9999999
    ty = 9999999
    ret = sol.reachingPoints(sx,sy,tx,ty)
    print(ret)