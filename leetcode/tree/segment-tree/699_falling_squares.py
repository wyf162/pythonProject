# _*_ coding: utf-8 _*_
# @Time : 2022/05/26 12:12 AM 
# @Author : yefe
# @File : 699_falling_squares
import collections


# todo
class Solution(object):
    def __init__(self):
        self.tree = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)

    def fallingSquares(self, positions):
        m = set()
        for i in range(len(positions)):
            l, r = positions[i][0], positions[i][0] + positions[i][1] - 1
            m |= {l, r}
        m = sorted(list(m))
        rank = {}
        r = 0
        for s in m:
            if s not in rank:
                rank[s] = r
                r += 1

        def query(s, e, l, r, id):  # query找到目前s,e覆盖区间的最高高度
            if s >= r or l >= e:
                return 0
            if s <= l < r <= e:
                return self.tree[id]
            else:
                mid = (l + r) // 2
                return max(self.lazy[id], query(s, e, l, mid, 2 * id + 1), query(s, e, mid, r, 2 * id + 2))

        def update(s, e, l, r, h, id=0):  # 更新l,r所在区间的最高高度
            if s >= r or l >= e:
                return
            if s <= l < r <= e:
                self.tree[id] = max(h, self.tree[id])
                self.lazy[id] = max(h, self.tree[id])
            else:
                mid = (l + r) // 2
                update(s, e, l, mid, h, 2 * id + 1)
                update(s, e, mid, r, h, 2 * id + 2)
                self.tree[id] = max(self.lazy[id], max(self.tree[2 * id + 1], self.tree[2 * id + 2]))

        ans = []
        for l, length in positions:
            L = rank[l]
            R = rank[l + length - 1]
            h = query(L, R + 1, 0, len(rank), 0) + length
            update(L, R + 1, 0, len(rank), h, 0)
            ans.append(self.tree[0])
        return ans


if __name__ == '__main__':
    sol = Solution()
    # positions = [[1, 2], [2, 3], [6, 1]]
    positions = [[9,7],[1,9],[3,1]]
    ret = sol.fallingSquares(positions)
    print(ret)
