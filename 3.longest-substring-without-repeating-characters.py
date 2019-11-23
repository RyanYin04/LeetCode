#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        ls = []
        head = 0
        for curr, ss in enumerate(s):
            if ss not in ls:
                ls.append(ss)
            elif ss in ls:
                idx = ls.index(ss)
                temp = len(ls)
                if temp > max_len:
                    max_len = temp
                ls = [ss]
        temp = len(ls)
        if temp > max_len:
            max_len = temp
        return max_len
                

        
        
# @lc code=end
s = Solution()

a = 'pwwkew'
s.lengthOfLongestSubstring(a)
