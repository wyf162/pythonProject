# _*_ coding: utf-8 _*_
# @Time : 2022/10/21 9:17 PM 
# @Author : yefe
# @File : 901_StockSpanner

class StockSpanner:

    def __init__(self):
        self.stk = []
        self.cnt = 0

    def next(self, price: int) -> int:
        while self.stk and self.stk[-1][0] <= price:
            self.stk.pop()
        self.cnt += 1
        ret = self.cnt - (0 if not self.stk else self.stk[-1][1])
        self.stk.append((price, self.cnt))
        return ret


if __name__ == '__main__':
    cmds = ["StockSpanner", "next", "next", "next"]
    parms = [[], [50], [70], [70]]
    # [null,true,[],[1,0],[]]
    n = len(cmds)
    stock_spanner = StockSpanner()
    for i in range(1, n):
        ret = stock_spanner.next(*parms[i])
        print(ret)
