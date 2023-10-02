# _*_ coding: utf-8 _*_
# @Time : 2022/3/3 下午10:27 
# @Author : wangyefei
# @File : 2162_min_cost_set_time.py


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        ans = list()
        m = targetSeconds // 60
        s = targetSeconds % 60
        if m==0:
            ans.append(str(s))
        st_m = str(m)
        st_s = str(s)
        if len(st_s) < 2:
            st_s = '0' + st_s
        if len(str(m))<=2:
            ans.append(str(m) + st_s)
        if len(st_m + st_s) < 4:
            ans.append('0' + st_m + st_s)
        if m >= 1 and s < 40:
            m -= 1
            s += 60
            if m == 0:
                ans.append(str(s))
            ans.append(str(m) + str(s))
            if len(ans[-1]) < 4:
                ans.append('0' + ans[-1])
        print(ans)

        costs = list()
        for seqs in ans:
            cost = 0
            cur_at = str(startAt)
            for num in seqs:
                if num != cur_at:
                    cost = cost + moveCost + pushCost
                    cur_at = num
                else:
                    cost = cost + pushCost
            costs.append(cost)
        print(costs)
        return min(costs)


if __name__ == '__main__':
    sol = Solution()
    start_at = 1
    move_cost = 9403
    push_cost = 9402
    target_seconds = 6008
    ret = sol.minCostSetTime(start_at, move_cost, push_cost, target_seconds)
    print(ret)