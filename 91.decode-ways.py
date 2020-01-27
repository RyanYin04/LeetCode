#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = [0] * (l + 1)
        if not s or s[0] == '0':
            return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(2, l + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '2' or s[i - 2] == '1':
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if s[i-2] == '1' or ('1' <= s[i - 1]<= '6' and s[i- 2] == '2'):
                    dp[i] = dp[i-1] + dp[i- 2]
                else:
                    dp[i] = dp[i-1]
        return dp[-1]
        # 递归：
        # if len(s) == 0 or s[0] == '0':
        #     return 0
        # if len(s) == 1:
        #     return 1
        # if len(s) == 2:
        #     if int(s[0:2]) <= 26 :
        #         return 1 + (int(s[0:2]) >= 11 )
        #     else:
        #         return 0
        # return self.numDecodings(s[1:]) + self.numDecodings(s[2:]) * (int(s[0:2]) <= 26)


   
# @lc code=end
s = Solution()
s.numDecodings('223')
