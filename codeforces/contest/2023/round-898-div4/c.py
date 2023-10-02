# -*- coding : utf-8 -*-
# @Time: 2023/9/21 23:08
# @Author: yefei.wang
# @File: c.py
import sys

# sys.stdin = open('../input.txt', 'r')


points = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
          [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
          [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
          [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
          [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
          [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
          [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
          [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          ]


def solve(grid):
    point = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                point += points[i][j]
    print(point)


def main():
    tcn = int(input())
    for _ in range(tcn):
        grid = []
        for i in range(10):
            grid.append(input().strip('\r\n'))
        solve(grid)


if __name__ == '__main__':
    main()
