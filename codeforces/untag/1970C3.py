def main():
    n, q = readIntArr()

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = readIntArr()
        adj[u].append(v)
        adj[v].append(u)

    root = 1
    children = [[] for _ in range(n + 1)]
    order = [1]
    st = [(1, -1)]
    while st:
        u, p = st.pop()
        for v in adj[u]:
            if v != p:
                children[u].append(v)
                order.append(v)
                st.append((v, u))
    state = [0] * (n + 1)  # 1 for winning state, when considering routes to leaves
    order.reverse()
    for u in order:
        for v in children[u]:
            if state[v] == 0:
                state[u] = 1
                break

    # dfs from root
    state2 = [0] * (n + 1)
    state2[root] = state[root]
    st = [(root, -1, 1)]
    while st:
        u, p, p_state = st.pop()  # p_state is the state of p without the path to u
        u_win_cnts = 0
        if p_state == 0:
            u_win_cnts += 1
        for v in adj[u]:
            if v != p and state[v] == 0:
                u_win_cnts += 1
        if u_win_cnts >= 1:
            state2[u] = 1
        for v in adj[u]:
            if v != p:
                temp = u_win_cnts
                if state[v] == 0:
                    temp -= 1
                if temp >= 1:
                    st.append((v, u, 1))
                else:
                    st.append((v, u, 0))

    ans = [''] * q
    queries = readIntArr()
    for i, u in enumerate(queries):
        if state2[u] == 1:
            ans[i] = 'Ron'
        else:
            ans[i] = 'Hermione'
    multiLineArrayPrint(ans)

    return


import sys

input = sys.stdin.buffer.readline  # FOR READING PURE INTEGER INPUTS (space separation ok)


# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.

def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))


def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))


def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))


def readIntArr():
    return [int(x) for x in input().split()]


# def readFloatArr():
#     return [float(x) for x in input().split()]

def makeArr(defaultValFactory, dimensionArr):  # eg. makeArr(lambda:0,[n,m])
    dv = defaultValFactory;
    da = dimensionArr
    if len(da) == 1:
        return [dv() for _ in range(da[0])]
    else:
        return [makeArr(dv, da[1:]) for _ in range(da[0])]


def queryInteractive(a, b, c):
    print('? {} {} {}'.format(a, b, c))
    sys.stdout.flush()
    return int(input())


def answerInteractive(x1, x2):
    print('! {} {}'.format(x1, x2))
    sys.stdout.flush()


inf = float('inf')
# MOD=10**9+7
# MOD=998244353

from math import gcd, floor, ceil
import math

# from math import floor,ceil # for Python2

for _abc in range(1):
    main()