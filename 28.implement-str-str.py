#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        lNeedle = len(needle)
        i = 0
        while i <= len(haystack) - lNeedle:
            if haystack[i:i+lNeedle] == needle:
                return i
            i += 1
        return -1
# @lc code=end

s = Solution()
s.strStr('hello', 'll')