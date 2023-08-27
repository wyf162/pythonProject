# _*_ coding: utf-8 _*_
# @Time : 2022/11/20 1:30 PM 
# @Author : yefe
# @File : 799_champagne_tower


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(1, query_row + 1):
            nextRow = [0] * (i + 1)
            for j, volume in enumerate(row):
                if volume > 1:
                    nextRow[j] += (volume - 1) / 2
                    nextRow[j + 1] += (volume - 1) / 2
            row = nextRow
        return min(1, row[query_glass])


if __name__ == '__main__':
    sol = Solution()
    poured = 2
    query_row = 1
    query_class = 1
    ret = sol.champagneTower(poured, query_row, query_class)
    print(ret)
