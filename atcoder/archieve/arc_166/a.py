import sys
sys.stdin = open('../../input.txt', 'r')

tcn = int(input())

NO = 'No'
YES = 'Yes'


def check(xaidxs, xcidxs, yaidxs):
    ai, ci = 0, 0
    cd = len(yaidxs) - len(xaidxs)
    if cd < 0 or cd > len(xcidxs):
        return False
    xaidxs = xaidxs + xcidxs[:cd]
    xaidxs.sort()
    for j in range(len(yaidxs)):
        if xaidxs[j] > yaidxs[j]:
            return False
    return True


for _tcn_ in range(tcn):
    n, X, Y = input().split()
    n = int(n)

    ycidxs = []
    ans = None
    for i in range(n):
        if Y[i] == 'C':
            if X[i] != 'C':
                ans = False
                break
            else:
                ycidxs.append(i)
    ycidxs.append(n)
    if ans is not None:
        print(NO)
        continue

    pre = 0
    for end in ycidxs:
        xaidxs = []
        xcidxs = []
        yaidxs = []
        for i in range(pre, end):
            if X[i] == 'A':
                xaidxs.append(i)
            elif X[i] == 'C':
                xcidxs.append(i)

            if Y[i] == 'A':
                yaidxs.append(i)

        tmp = check(xaidxs, xcidxs, yaidxs)
        if not tmp:
            ans = False
            break

        pre = end + 1

    print(YES if ans is None else NO)
