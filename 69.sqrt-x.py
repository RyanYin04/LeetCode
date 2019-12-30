#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        rpnt = x
        lpnt = 1
        while True:
            mid = (rpnt + lpnt) //2
            if mid**2 > x:
                rpnt = mid
            elif (mid+1)**2 <= x:
                lpnt = mid
            elif mid**2 < x and (mid + 1)**2 > x or mid**2 == x:
                return mid
        
        
# @lc code=end

s = Solution()
s.mySqrt(36)