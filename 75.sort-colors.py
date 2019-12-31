#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using selection sort:
        if len(nums) <= 1:
            return nums
        for currPnt in range(1, len(nums)):
            pnt = 0
            while pnt < currPnt:
                if nums[currPnt] <= nums[pnt]:
                    nums[pnt], nums[pnt + 1:currPnt + 1] = nums[currPnt], nums[pnt:currPnt]
                    break
                pnt += 1
# @lc code=end
s = Solution()
nums = [2,1,1,2,0,0,2,0,0,2,1,1]
s.sortColors(nums)
nums
