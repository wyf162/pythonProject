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
node = 'AAA'
rst = 0
for _ in range(100000):
    print(node)
    D = 0 if S[i] == 'L' else 1
    node = nodes[node][D]
    rst += 1
    if node == 'ZZZ':
        break
    i += 1
    i %= M

print(rst)
