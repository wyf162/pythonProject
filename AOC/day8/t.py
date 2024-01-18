import itertools

nums = [[1, 2, 3], [4, 5, 6]]

for perm in itertools.product(*nums):
    print(perm)