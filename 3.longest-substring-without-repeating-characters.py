#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        else:
            if s[0] == s[1]:
                return lengthOfLongestSubstring(s[1:])
            else:
                return 
        
        return 

        
# @lc code=end
s = Solution()

a = 'abcabcbb'
s.lengthOfLongestSubstring(a)