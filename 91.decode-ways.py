#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            if int(s) >= 1:
                return 1
            else:
                return 0
        if len(s) == 2:
            if int(s) >= 27 or int(s) <= 10:
                if int(s) <= 20 and int(s) > 9:
                    return 1
                if s[1] == '0' or int(s) <= 9:
                    return 0
                else:
                    return 1
            if int(s) < 27 and int(s) > 10:
                return 2
            
        return self.numDecodings(s[1:]) + self.numDecodings(s[2:]) * (int(s[0:2]) <= 26)
        
# @lc code=end
s = Solution()
s.numDecodings('27')
