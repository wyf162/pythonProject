# _*_ coding: utf-8 _*_
# @Time : 2021/11/19 上午7:05 
# @Author : wangyefei
# @File : dfs.py
class Solution:
    def integerReplacement(self, n: int) -> int:
        self.ans = float('inf')

        def dfs(num, cnt):
            print(num,cnt)
            if num == 1:
                print(cnt)
                self.ans = min(self.ans, cnt)
            elif num > 1:
                if num % 2 == 0:
                    dfs(num>>1, cnt + 1)
                else:
                    dfs(num + 1, cnt + 1)
                    dfs(num - 1, cnt + 1)

        dfs(n, 0)
        return int(self.ans)


if __name__ == "__main__":
    sol = Solution()
    print(sol.integerReplacement(8))
