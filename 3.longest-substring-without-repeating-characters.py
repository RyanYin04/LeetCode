#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for idx, ss in enumerate(s):
            if idx == len(s) - 1:
                l = max(l, 1)
                break
            if ss in s[idx+1:]:
                l = max(l, s[idx+1:].index(ss)+1)
            elif ss not in s[idx+1:]:
                return max(l, len(s) - idx)
        
        return l

        
# @lc code=end
s = Solution()

a = 'abcabcbb'
s.lengthOfLongestSubstring(a)