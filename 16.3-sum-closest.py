#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) <= 2:
            return None 
        cVal = sum(nums[0:3])
        nums.sort()
        for i, a in enumerate(nums):
            lpnt = i + 1
            rpnt = len(nums) - 1
            while lpnt < rpnt:
                b = nums[lpnt]
                c = nums[rpnt]
                currVal = a + b + c
                if currVal == target:
                    return target
                if abs(currVal - target) < abs(cVal - target):
                    cVal = currVal
                else:
                    if currVal - target > 0:
                        rpnt -= 1
                    if currVal - target < 0:
                        lpnt += 1
        return cVal


            

            
        
# @lc code=end