#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I':1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        
        keys = symbol.keys()
        val = symbol[s[-1]]
        
        for i in range(len(s) - 2, -1, -1):
            temp =  symbol[s[i]]
            if symbol[s[i +1]] > temp:
                temp = -temp
            val += temp
        return val
        
# @lc code=end

