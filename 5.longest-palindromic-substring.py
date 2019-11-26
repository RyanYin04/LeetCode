#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxS = ''
        maxL = 0
        for i in range(len(s)):
            ## Treat each element as the middle of a palindrome string.
            ## And there is two conditions:
            ### One is the palidrome string to be returned has an odd lenth, the other is that the length is even.
            maxS = max(self.helper(s, i, i), self.helper(s, i, i+1), maxS, key = len)
            maxL = len(s)
        return maxS
    
    def helper(self, s, lm, rm):
        ## Hleper function returns the palindrome subsrting by set the left middle point and right middle point as well as the string to be searched.
        while lm >= 0 and rm <len(s) and s[lm] == s[rm] :
            lm -= 1
            rm += 1
        return s[lm+1: rm]

# @lc code=end