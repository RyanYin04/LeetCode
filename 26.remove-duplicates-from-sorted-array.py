#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 1:
            return len(nums)
        currPnt = 1
        currVal = nums[0]
        l = 1
        for i in range(1, len(nums)):
            if nums[i] > currVal:
                nums[currPnt] = nums[i]
                currVal = nums[i]
                currPnt += 1
                l += 1
            if nums[i] < currVal:
                break
            
        return l
# @lc code=end