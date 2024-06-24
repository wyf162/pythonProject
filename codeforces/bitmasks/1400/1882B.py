# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = int(input())

for _tcn_ in range(tcn):
    n = I()

    nums = []
    for i in range(n):
        num = 0
        for k in LI()[1:]:
            num |= (1 << k)
        nums.append(num)

    boss = 0
    for num in nums:
        boss |= num

    ans = 0
    for b in range(1, 51):
        t = 0
        for num in nums:
            if num >> b & 1:
                continue
            else:
                t |= num
        if t != boss and bin(t).count('1') > ans:
            ans = bin(t).count('1')
            # print(b, bin(t))
            # print(b, bin(t))
    print(ans)
