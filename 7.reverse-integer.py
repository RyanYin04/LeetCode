#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ## Just use the feature support by python
        flag = (x > 0) - ( x < 0 )
        x_rev = int(str(flag * x)[::-1])
        return flag * x_rev * (x_rev <= 2**31 - 1)    
# @lc code=end

