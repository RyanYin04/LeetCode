#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        head = 0
        ls = []
        for ss in s:
            if ss not in ls:
                ls.append(ss)
            elif ss in ls:
                head = ls.index(ss)
                temp = len(ls)
                ls = ls[head+1:]
                ls.append(ss)
                if temp > max_len:
                    max_len = temp
                
        temp = len(ls)
        if temp > max_len:
            max_len = temp
        return max_len
                

        
        
