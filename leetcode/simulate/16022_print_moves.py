# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 9:37 AM 
# @Author : yefe
# @File : 16022_print_moves
from typing import List


class Solution:
    clockwise = {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}
    anticlockwise = {'R': 'U', 'U': 'L', 'L': 'D', 'D': 'R'}
    color = {'X': '_', '_': 'X'}
    move = {'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)}

    def printKMoves(self, k: int) -> List[str]:
        hst = dict()
        cur = (0, 0, 'R')
        max_h, min_h = 0,0
        max_v, min_v = 0,0
        for _ in range(k):
            x, y, d = cur
            if (x, y) not in hst:
                tag = '_'
                hst[(x, y)] = 'X'
            else:
                tag = hst[(x, y)]
                hst[(x, y)] = self.color[hst[(x, y)]]
            if tag == '_':
                d = self.clockwise[d]
            else:
                d = self.anticlockwise[d]
            dx, dy = self.move[d]
            x, y = x + dx, y + dy
            cur = (x, y, d)
            if x>max_h:
                max_h = x
            if x<min_h:
                min_h = x
            if y>max_v:
                max_v = y
            if y<min_v:
                min_v = y
        h = max_h-min_h+1
        v = max_v-min_v+1
        res = [['_' for j in range(h)] for i in range(v)]
        for y in range(max_v, min_v-1, -1):
            for x in range(min_h, max_h + 1, 1):
                abs_h = x - min_h
                abs_v = max_v - y
                res[abs_v][abs_h] = hst.get((x, y), '_')
        abs_h = cur[0]-min_h
        abs_v = max_v - cur[1]
        res[abs_v][abs_h] = cur[2]
        return [''.join(tmp) for tmp in res]

    def printKMoves2(self, k: int) -> List[str]:
        hst = dict()
        cur = (0, 0, 'R')
        while k > 0:
            x, y, d = cur
            if (x, y) not in hst:
                tag = '_'
                hst[(x, y)] = 'X'
            else:
                tag = hst[(x, y)]
                hst[(x, y)] = self.color[hst[(x, y)]]
            if tag == '_':
                d = self.clockwise[d]
            else:
                d = self.anticlockwise[d]
            dx, dy = self.move[d]
            x, y = x + dx, y + dy
            cur = (x, y, d)
            k = k - 1
        l = min([x for x, y in hst.keys()] + [cur[0]])
        r = max([x for x, y in hst.keys()] + [cur[0]])
        d = min([y for x, y in hst.keys()] + [cur[1]])
        u = max([y for x, y in hst.keys()] + [cur[1]])
        res = []
        for y in range(u, d-1, -1):
            tmp = ""
            for x in range(l, r + 1, 1):
                if (x, y) == (cur[0], cur[1]):
                    tmp += cur[2]
                else:
                    tmp += hst.get((x, y), '_')
            res.append(tmp)
        return res


if __name__ == '__main__':
    sol = Solution()
    k = 16
    ret = sol.printKMoves(k)
    print(ret)
