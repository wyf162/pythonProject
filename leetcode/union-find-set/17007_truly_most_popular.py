# _*_ coding: utf-8 _*_
# @Time : 2022/05/01 6:01 PM 
# @Author : yefe
# @File : 17007_truly_most_popular
import collections
from typing import List
from functools import lru_cache
from collections import defaultdict

from collections import defaultdict


class UnionFind(object):
    def __init__(self, names):
        self.parent = {}
        for name in names:
            self.parent[name] = name

    def union(self, a, b):
        if a not in self.parent:
            self.parent[a] = a
        if b not in self.parent:
            self.parent[b] = b
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a < root_b:
            self.parent[root_b] = root_a
        else:
            self.parent[root_a] = root_b

    def find_root(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node


class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        leetcode17.07
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        # 频率map
        freq_map = defaultdict(int)
        for name_freq in names:
            name, freq_str = (part.strip().strip(')') for part in name_freq.split('('))
            freq_map[name] = int(freq_str)
        # 初始化并查集
        uf = UnionFind(freq_map.keys())
        # 并操作
        for pair_str in synonyms:
            a, b = (name.strip().strip(')').strip('(') for name in pair_str.split(','))
            uf.union(a, b)
        # 生成结果
        result = []
        res_map = defaultdict(int)
        for name, freq in freq_map.items():
            res_map[uf.find_root(name)] += freq
        for name, freq in res_map.items():
            result.append('{}({})'.format(name, freq))
        result.sort()
        return result


class Solution2:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        hst = defaultdict(list)
        for synonym in synonyms:
            name1, name2 = synonym[1:-1].split(',')
            hst[name1].append(name2)
            hst[name2].append(name1)

        def bfs(name):
            q = collections.deque()
            q.append(name)
            vis = set()
            vis.add(name)
            while q:
                node = q.popleft()
                for nex in hst[node]:
                    if nex not in vis:
                        q.append(nex)
                        vis.add(nex)
            return vis

        visited = set()
        new_hst = dict()
        for k in hst.keys():
            # print(k)
            if k not in visited:
                keys = bfs(k)
                visited |= keys
                keys = list(keys)
                min_key = min(keys)
                for key in keys:
                    new_hst[key] = min_key

        res_hst = defaultdict(int)
        for name in names:
            name, cnt = name[:-1].split('(')
            cnt = int(cnt)
            if name in new_hst:
                res_hst[new_hst[name]] += cnt
            else:
                res_hst[name] += cnt

        res = [k+'('+str(v)+')' for k, v in res_hst.items()]
        res.sort()
        return res


if __name__ == '__main__':
    # names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
    # synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
    names = ["Fcclu(70)", "Ommjh(63)", "Dnsay(60)", "Qbmk(45)", "Unsb(26)", "Gauuk(75)", "Wzyyim(34)", "Bnea(55)", "Kri(71)",
     "Qnaakk(76)", "Gnplfi(68)", "Hfp(97)", "Qoi(70)", "Ijveol(46)", "Iidh(64)", "Qiy(26)", "Mcnef(59)", "Hvueqc(91)",
     "Obcbxb(54)", "Dhe(79)", "Jfq(26)", "Uwjsu(41)", "Wfmspz(39)", "Ebov(96)", "Ofl(72)", "Uvkdpn(71)", "Avcp(41)",
     "Msyr(9)", "Pgfpma(95)", "Vbp(89)", "Koaak(53)", "Qyqifg(85)", "Dwayf(97)", "Oltadg(95)", "Mwwvj(70)", "Uxf(74)",
     "Qvjp(6)", "Grqrg(81)", "Naf(3)", "Xjjol(62)", "Ibink(32)", "Qxabri(41)", "Ucqh(51)", "Mtz(72)", "Aeax(82)",
     "Kxutz(5)", "Qweye(15)", "Ard(82)", "Chycnm(4)", "Hcvcgc(97)", "Knpuq(61)", "Yeekgc(11)", "Ntfr(70)", "Lucf(62)",
     "Uhsg(23)", "Csh(39)", "Txixz(87)", "Kgabb(80)", "Weusps(79)", "Nuq(61)", "Drzsnw(87)", "Xxmsn(98)", "Onnev(77)",
     "Owh(64)", "Fpaf(46)", "Hvia(6)", "Kufa(95)", "Chhmx(66)", "Avmzs(39)", "Okwuq(96)", "Hrschk(30)", "Ffwni(67)",
     "Wpagta(25)", "Npilye(14)", "Axwtno(57)", "Qxkjt(31)", "Dwifi(51)", "Kasgmw(95)", "Vgxj(11)", "Nsgbth(26)",
     "Nzaz(51)", "Owk(87)", "Yjc(94)", "Hljt(21)", "Jvqg(47)", "Alrksy(69)", "Tlv(95)", "Acohsf(86)", "Qejo(60)",
     "Gbclj(20)", "Nekuam(17)", "Meutux(64)", "Tuvzkd(85)", "Fvkhz(98)", "Rngl(12)", "Gbkq(77)", "Uzgx(65)", "Ghc(15)",
     "Qsc(48)", "Siv(47)"]
    synonyms = ["(Gnplfi,Qxabri)", "(Uzgx,Siv)", "(Bnea,Lucf)", "(Qnaakk,Msyr)", "(Grqrg,Gbclj)", "(Uhsg,Qejo)", "(Csh,Wpagta)",
     "(Xjjol,Lucf)", "(Qoi,Obcbxb)", "(Npilye,Vgxj)", "(Aeax,Ghc)", "(Txixz,Ffwni)", "(Qweye,Qsc)", "(Kri,Tuvzkd)",
     "(Ommjh,Vbp)", "(Pgfpma,Xxmsn)", "(Uhsg,Csh)", "(Qvjp,Kxutz)", "(Qxkjt,Tlv)", "(Wfmspz,Owk)", "(Dwayf,Chycnm)",
     "(Iidh,Qvjp)", "(Dnsay,Rngl)", "(Qweye,Tlv)", "(Wzyyim,Kxutz)", "(Hvueqc,Qejo)", "(Tlv,Ghc)", "(Hvia,Fvkhz)",
     "(Msyr,Owk)", "(Hrschk,Hljt)", "(Owh,Gbclj)", "(Dwifi,Uzgx)", "(Iidh,Fpaf)", "(Iidh,Meutux)", "(Txixz,Ghc)",
     "(Gbclj,Qsc)", "(Kgabb,Tuvzkd)", "(Uwjsu,Grqrg)", "(Vbp,Dwayf)", "(Xxmsn,Chhmx)", "(Uxf,Uzgx)"]
    sol = Solution()
    ret = sol.trulyMostPopular(names, synonyms)
    print(ret)

    sol = Solution2()
    ret = sol.trulyMostPopular(names, synonyms)
    print(ret)
