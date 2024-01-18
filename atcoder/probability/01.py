mod = 998244353


def invmod(x):
    return pow(x, mod - 2, mod)


# a * x = b (mod n)
# 从区间[0,n-1] 求 x
# 当a和x互素时，可以求a的逆元a-1
# x = b * a-1 (mod n)

# 分数a/b
a, b = 2, 3
invN = invmod(b)
rst = a * invN % mod
print(rst)

n = 2
xs = [1, 1]
ys = [3, 3]
rst = 0
for i in range(2):
    rst += xs[0]
