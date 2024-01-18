import itertools
import math
import sys

# sys.stdin = open('./demo.txt', 'r')
sys.stdin = open('./input.txt', 'r')
nodes = dict()

S = input()
M = len(S)
N = 714
for i in range(N):
    s = input()
    s1, s2, s3 = s[:3], s[7:10], s[12:15]
    nodes[s1] = [s2, s3]

i = 0
node_list = [k for k, v in nodes.items() if k.endswith('A')]
print(node_list)

nn = [[node_list[i]] for i in range(len(node_list))]
is_circle = [0] * len(nn)

for _ in range(100000):
    # print(node_list)
    D = 0 if S[i] == 'L' else 1
    for j in range(6):
        if is_circle[j]:
            continue
        nn[j].append(nodes[nn[j][-1]][D])
        if nn[j][0] == nn[j][-1]:
            is_circle[j] = 1

    if all(is_circle):
        break
    i += 1
    i %= M

nums = [[] for _ in range(6)]

for i in range(6):
    for j in range(len(nn[i])):
        if nn[i][j].endswith('Z'):
            nums[i].append(j)
            print(j, end=' ')
    print()

rst = 22177804543097711145667751
# print(nums)
for prd in itertools.product(*nums):
    ret = math.lcm(*prd)
    rst = min(rst, ret)
print(rst)

# print(rst)
# 21883 * 19667 * 19667 * 16897 * 13019 * 11911
