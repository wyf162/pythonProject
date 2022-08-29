# _*_ coding: utf-8 _*_
# @Time : 2022/08/23 9:11 PM 
# @Author : yefe
# @File : 1987_number_of_unique_good_subsequences


# func numberOfUniqueGoodSubsequences(s string) int {
# 	const mod int = 1e9 + 7
# 	f := [2]int{}
# 	for i := len(s) - 1; i >= 0; i-- {
# 		f[s[i]&1] = (f[0] + f[1] + 1) % mod
# 	}
# 	ans := f[1]
# 	if strings.Contains(s, "0") {
# 		ans = (ans + 1) % mod
# 	}
# 	return ans
# }


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10 ** 9 + 7

        f = [0]*2
        for a in reversed(binary):
            f[int(a) & 1] = (f[0]+f[1]+1)%MOD

        ans = f[1]
        if '0' in binary:
            ans += 1
            ans %= MOD
        return ans


if __name__ == '__main__':
    sol = Solution()
    binary = "101"
    ret = sol.numberOfUniqueGoodSubsequences(binary)
    print(ret)
