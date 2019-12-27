#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums):
        if len(nums) <= 1:
            return True
        maxVal = 0
        for i in range(len(nums) - 1):
            if maxVal < i:
                return False
            else:
                maxVal = max(maxVal, nums[i] + i)
        return (maxVal >= len(nums) - 1)


        
# @lc code=end

s = Solution()
s.canJump([3,2,1,0,4])