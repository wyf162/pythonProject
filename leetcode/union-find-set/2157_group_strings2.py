# -*- coding : utf-8 -*-
# @Time: 2022/8/12 23:35
# @Author: yefei.wang
# @File: 2157_group_strings2.py
import sys
from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # 并查集模板（哈希表写法）
        fa, size = {}, defaultdict(int)
        groups, max_size = len(words), 0

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def merge(x: int, y: int):
            nonlocal groups, max_size
            if y not in fa:
                return
            print(x, y)
            x, y = find(x), find(y)
            if x == y:
                return
            fa[x] = y
            size[y] += size[x]
            max_size = max(max_size, size[y])  # 维护答案
            groups -= 1

        for word in words:
            x = 0
            for ch in word:
                x |= 1 << (ord(ch) - ord('a'))  # 计算 word 的二进制表示
            fa[x] = x  # 添加至并查集
            size[x] += 1
            max_size = max(max_size, size[x])  # 维护答案
            if size[x] > 1:
                groups -= 1

        for x in fa:  # 枚举所有字符串（二进制表示）
            for i in range(26):
                merge(x, x ^ (1 << i))  # 添加或删除字符 i
                if (x >> i) & 1:
                    for j in range(26):
                        if ((x >> j) & 1) == 0:
                            merge(x, x ^ (1 << i) | (1 << j))  # 替换字符 i 为 j
        return [groups, max_size]


if __name__ == '__main__':

    sys.stderr = sys.stdout = open('./other.log', 'w')

    sol = Solution()
    # words = ["a", "ab", "ab", "bdc"]
    words = ["umeihvaq", "ezflcmsur", "ynikwecaxgtrdbu", "u", "q", "gwrv", "ftcuw", "ocdgslxprzivbja", "zqrktuepxs",
             "cpqolvnwxz", "geqis", "xgfdazthbrolci", "vwnrjqzsoepa", "udzckgenvbsty", "lpqcw", "nekpvchqfgdo",
             "iapjhxvdrmwetz", "gw", "waxokchnmifsruj", "vqp", "vbpkij", "ufjvbstzh", "swiu", "knslbdcahfrox",
             "ctofplkhednmv", "g", "zk", "idretzjbpl", "pxqdauys", "mfgrqaktbzpv", "vdtq", "wyxjrcie", "kl", "jpcdzmli",
             "oth", "yumdawhfbskcjo", "rvfksqhu", "swemnvjpg", "rnl", "zgd", "rmzdbcsqht", "ure", "qlusoaxprtebn",
             "zkbmvtpya", "jszxuwevfidkm", "smlft", "cpwugmbzfsqr", "cblkjevhp", "iyfnozaulex", "qvlok", "wsgm", "du",
             "awyplckj", "aey", "ycsjqnt", "vtoqzsyx", "ejqixsmrdhlofyp", "kvlmurbzjg", "lysdahgpwmrcn", "af",
             "jkezhdu", "etjzqiyghdnovm", "ycwdfnluoke", "kwshbx", "pyvaznljqwes", "xakinu", "e", "zjexfgvhtabwcy",
             "thuvwlnjkbxym", "jorzeslpidmhubq", "wnr", "qzdv", "qeovrbmwzgpdh", "jkioenptaygfubh", "bvndzxijope",
             "cudizhjntbes", "rnhzitpqoexwb", "ihezcmfqouyl", "q", "mwtsdjqn", "hrmc", "hxaocbyikluvqsf", "d",
             "vgwjzuaondbcm", "ibqxltf", "rzyhguptmesqo", "ruwgy", "jvprwhtzuf", "aupngodjexkiw", "yhijelwpvtsrbqc",
             "gtick", "koilywcfbs", "elv", "dehxzlitskq", "ptvbkql", "msfxyjahlzo", "oslxzfwrpmtyh", "gypuchkwa",
             "rsqij", "tw", "igbcylqfhtmjkr", "nryhzjgi", "pw", "bnfairow", "xjzrf", "olxfypjtmrncuv", "ifhue",
             "akcvofuyzwbj", "tvhxfeuiykpwbsz", "wnrztclfpm", "ozvypnfwrqg", "cwkgr", "gjyzrucplbsfe", "pdtzmfoy",
             "wehd", "bnvqhcmg", "uyw", "sgynxljqbf", "tvxbq", "wcmguioelbdrkvx", "okvtyexuj", "hjbc", "uidcswzm",
             "jemtkvshizaub", "rmb", "jpgnqdemzcxa", "dmalekhiyj", "akocedu", "rlpqufcv", "r", "lohgs", "xapnorj",
             "cdb", "icopdtzxy", "xcrflvojqgpkwt", "elv", "rp", "yv", "u", "atdxqeilhkg", "olfvmrgkb", "rplxskabvtqmhw",
             "n", "rldswkyoujmfxpn", "rvgejzdusoya", "hvoft", "wskgmjchz", "luagnzkj", "ywe", "i", "wcqtsk",
             "umpvywknjbxacsd", "ynavjpcrgq", "jyftmklci", "xfol", "zh", "kut", "zvawyielscotkn", "p", "wykpqdjoz",
             "uabtpxkvq", "uabtifwhrvxc", "sdcamqup", "srghwfptloxvke", "sfdywtx", "tuohnxzjqmac", "pwxjyhdurnfz",
             "axgfcuqtiyhjz", "rwqpyh", "bmoznqavicdgp", "jcu", "vnkc", "jpb", "nvfqyahjkul", "radpctwixygb", "pvjmk",
             "s", "dzyqjbwucne", "mgh", "ivc", "eaqc", "yjimsadtcwbgk", "lo", "ayirlsfevtwpnd", "wcsk", "xlvejy",
             "kcjrqf", "a", "ixsdga", "vk", "cqxyfotziwrvl", "zmxboiewhfdjlnr", "kdpwngf", "zyretijxpw", "ncw", "ljw",
             "mrxeciy", "aqwcofnjypsgi", "byuvhj", "ukidyqzhxgowmc", "cpqsmu", "auwmcrpdisbzokg", "pxgwmvfq",
             "azgljrsyeqwxfic", "xmlgpdrzwqe", "emgdcqntjpwrf", "hrwq", "zmjkx", "npabcide", "dvlfxnt", "kilqsvmborf",
             "lvsxjnbimhpzfow", "sqcym", "tcjmkwq", "yugkwdzvmteon", "pq", "nklmb", "azqcnodkimtxve", "ovpcfe",
             "uqkcwjimbvdyx", "xvdazh", "xk"]
    print(len(words))
    print(len(set(words)))
    ret = sol.groupStrings(words)
    print(ret)
    s = "abc"
    print(set(s))
