## DP

| 类型      | 题目                                                                                                          | 关键点                |
|---------|-------------------------------------------------------------------------------------------------------------|--------------------|
| 背包dp    | [樱花](https://www.luogu.com.cn/problem/P1833)                                                                | 多重背包 二进制优化         |
|         | [Color](https://www.luogu.com.cn/problem/P9688?contestId=133572)                                            | 离散化建模，不相交转移        |
|         | [Flip and Adjust](https://atcoder.jp/contests/abc271/tasks/abc271_d)                                        | 记录转移路径，倒推选择方案      |
|         | [摆花](https://www.luogu.com.cn/problem/P1077)                                                                | 滚动数组优化空间复杂度        |
|         | [金明的预算方案](https://www.luogu.com.cn/problem/P1064)                                                           | 树形依赖背包             |
| 序列DP    | [等差数组子序列](https://leetcode.cn/problems/arithmetic-slices-ii-subsequence/description/)                       |                    |
|         | [大师](https://www.luogu.com.cn/problem/P4933)                                                                |                    |
|         | [Sereja and Sequence](https://codeforces.com/contest/314/problem/C)                                         | LIS 去重             |
| DAG上DP  | [Count Restricted Paths](https://leetcode.cn/problems/number-of-restricted-paths-from-first-to-last-node/)  |
|         | [Largest Path Value](https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/description/)     |
| 树形DP    | [金明的预算方案](https://www.luogu.com.cn/problem/P1064)                                                           | 树形依赖背包             |
|         | [选课](https://www.luogu.com.cn/record/127297160)                                                             | 树形DP 后序dfs 先选父节点   |
|         | [在树上执行操作的最大分数](https://leetcode.cn/problems/maximum-score-after-applying-operations-on-a-tree/description/) |
| 状态机DP   | [买卖股票](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description)                        |                    |
| 状态压缩    | [关灯问题](https://www.luogu.com.cn/problem/P2622)                                                              | 优先队列优化转移方程         |
| CF1950G | [Shuffing Sangs](https://codeforces.com/contest/1950/problem/G)                                             | n^2*2^n(n=16)      |
| CF1102F | [Elongated Matrix](https://codeforces.com/contest/1102/problem/F)                                           | n^2*2^n(n=16) 子集DP |
| AT348F  | [Oddly Similar](https://atcoder.jp/contests/abc348/tasks/abc348_f)                                          | todo    状压优化       |
| 方案数     | [Playist](https://atcoder.jp/contests/abc323/tasks/abc323_e)                                                | 期望概率               | 
| 优化DP    | [执行操作使两个字符串相等](https://leetcode.cn/problems/apply-operations-to-make-two-strings-equal/description/)        | 贪心                 | 
|         | [带限制的子多集合的数目](https://leetcode.cn/problems/count-of-sub-multisets-with-bounded-sum/description/)            | 前缀和优化              |
|         | [子数组不同元素个数的平方和](https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-ii/)                 | 线段树DP              |
| LC3116  | [划分数组得到最小值之和](https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/solutions/)              | DP 单调队列            |
| 矩阵乘法    | [Neural Network Country](https://codeforces.com/problemset/problem/852/B)                                   | 快速矩阵乘  todo        |
| 期望DP    | [Assimilation IV](https://codeforces.com/problemset/problem/1525/E)                                         | todo 组合数学 期望DP     |

## Greedy

| 类型     | 题目                                                                      | 关键点    |
|--------|-------------------------------------------------------------------------|--------|
| 贪心     | [分组](https://www.luogu.com.cn/problem/P4447)                            | 优先队列模拟 |
| CF922D | [Robot Vacuum Cleaner](https://codeforces.com/problemset/problem/922/D) | 邻项交换法  |

## Graph Theory

| 类型   | 题目                                                                                                            | 关键点               |
|------|---------------------------------------------------------------------------------------------------------------|-------------------|
| 拓扑排序 |                                                                                                               |                   |
| 最短路  | [min Cost](https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/solutions/)                 |                   |
| 最短路  | [Buy a Ticket](https://codeforces.com/problemset/problem/938/D)                                               | Dijkstra          |
| 最短路  | [Pokeman Arena](https://codeforces.com/problemset/problem/1936/C)                                             | 最短路 建图优化 Dijkstra |
| 基环树  | [count Visited Nodes](https://leetcode.cn/problems/count-visited-nodes-in-a-directed-graph/description/)      |
|      | [maximum Invitations](https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/description/) |                   |
|      | [Mad City](https://codeforces.com/problemset/problem/1873/H)                                                  |                   |
| DFS  | [Fish Graph](https://codeforces.com/problemset/problem/1817/B)                                                | DFS找环             |
| 有向图  | [How Many Path](https://codeforces.com/contest/1547/problem/G)                                                | 强连通分量             |

## Tree

| 类型      | 题目                                                                                                       | 关键点       |
|---------|----------------------------------------------------------------------------------------------------------|-----------|
| 二叉搜索树   | [num Of Ways](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/) |
| 二叉树     | [distribute Coins](https://leetcode.cn/problems/distribute-coins-in-binary-tree/)                        |
| CF1491E | [Fib-Tree](https://codeforces.com/contest/1491/problem/E)                                                | fib推论     |
| 树的构造和遍历 | [Transpose](https://atcoder.jp/contests/abc350/tasks/abc350_f)                                           | 树的遍历      |
| CF500D  | [New Year Santa Network](https://codeforces.com/problemset/problem/500/D)                                | todo 边的权重 |

## bitwise

| 类型   | 题目                                                                                                              | 关键点 |
|------|-----------------------------------------------------------------------------------------------------------------|-----|
| 异或   |                                                                                                                 |
| 分位统计 |                                                                                                                 |     |
|      | [对数组执行操作使平方和最大](https://leetcode.cn/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/) | 贪心  |

## binary-search

| 类型 | 题目                                                             | 关键点 |
|----|----------------------------------------------------------------|-----|
|    | [Binary Search](https://codeforces.com/contest/1945/problem/E) | 二分  |

## divided and doubling

| 类型          | 题目                                                                     | 关键点            |
|-------------|------------------------------------------------------------------------|----------------|
| divided 分治  |                                                                        |                |
|             | [逆序对](https://www.luogu.com.cn/problem/P1908)                          | 归并排序，逆序对       |
|             | [Infinite Inversions](https://codeforces.com/problemset/problem/540/E) | 树状数组，逆序对       |
| doubling 倍增 |                                                                        |                |
| CF1148D     | [Alyona and a tree](https://codeforces.com/contest/1148/problem/D)     | 子树，倍增，二分  todo |
| CF1142B     | [Lynyrd Skynyrd](https://codeforces.com/problemset/problem/1142/B)     | 倍增，线段树 todo    |
| LGP7167     | [Fountain](https://www.luogu.com.cn/problem/P7167)                     | 单调栈 倍增         |

## Data Structure

| 类型                 | 题目                                                                | 关键点     |
|--------------------|-------------------------------------------------------------------|---------|
| disjoint set union | [BOX](https://atcoder.jp/contests/abc279/tasks/abc279_f)          | 模拟      |
| ListNode           | [Berserk Monsters](https://codeforces.com/contest/1922/problem/D) | 模拟 todo |

## 构造题

| 类型 | 题目                                                                   | 关键点                |
|----|----------------------------------------------------------------------|--------------------|
|    | [Amr and Chemistry](https://codeforces.com/problemset/problem/558/C) | 图 树 最短路/最长匹配前缀 中位数 |
|    | [Dogeforces](https://codeforces.com/contest/1494/problem/D)          | 递归构造               |

## 数学

| 类型   | 题目                                                                        | 关键点           |
|------|---------------------------------------------------------------------------|---------------|
| 组合数学 | [Product Transformation](https://codeforces.com/problemset/problem/852/F) | 组合数学 逆元 求余    |
| 组合数学 | [Devu and Flowers](https://codeforces.com/problemset/problem/451/E)       | 容斥原理 至少n个     |
| 康托展开 | [Permutations Summation](https://codeforces.com/contest/501/problem/D)    | 阶乘 逆序对 树状数组二分 |
| 裴蜀定理 | [Infinite Fence](https://codeforces.com/contest/1260/problem/C)           | 裴蜀定理 gcd      |

## MISC

| 类型 | 题目                                                                                   | 关键点     |
|----|--------------------------------------------------------------------------------------|---------|
| 排列 | [我算算算](https://ac.nowcoder.com/acm/contest/82758/H)                                  | mex     |
| 排列 | [统计逆序对方案数](https://leetcode.cn/problems/count-the-number-of-inversions/description/) | 逆序对     |
| 排列 | [Lucky Permutation](https://codeforces.com/problemset/problem/1768/D)                | 逆序对 并查集 |
| 排列 | [Permutations Summation](https://codeforces.com/problemset/problem/501/D)            | 康托展开    |
| 排列 | [Permutation Addicts](https://codeforces.com/contest/1738/problem/D)                 |         |
| 排列 | [Restore the Permutation](https://codeforces.com/contest/1759/problem/G)             | 字典序     |