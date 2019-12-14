#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.replace(' ', '')
        idx = 0
        res = ''
        if s[idx] == '+' or s[idx] == '-'
            res += s[idx]
            idx += 1
        while ord(s[idx]) > 48 and ord(s[idx]) < 57:
            res += s[idx]
            idx += 1
# @lc code=end

