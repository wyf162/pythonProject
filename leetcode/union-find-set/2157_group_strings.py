# -*- coding : utf-8 -*-
# @Time: 2022/8/12 21:10
# @Author: yefei.wang
# @File: 2157_group_strings.py
from typing import List


class UnionFind:

    def __init__(self, n: int):
        self.parent = [_ for _ in range(n)]
        self.size = [1 for _ in range(n)]
        self.group = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.group -= 1
        return True


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self.are_connected(words[i], words[j]):
                    print(i, j)
                    uf.merge(i, j)

        return [uf.group, max(uf.size)]

    @staticmethod
    def are_connected(a: str, b: str) -> bool:
        a = set(a)
        b = set(b)
        if len(a) + 1 == len(b) and len(a & b) == len(a):
            return True
        if len(a) - 1 == len(b) and len(a & b) == len(b):
            return True
        if len(a) == len(b) and len(a & b) == len(a) - 1:
            return True
        return False


if __name__ == '__main__':
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
