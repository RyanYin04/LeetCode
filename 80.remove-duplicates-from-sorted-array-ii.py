#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        # 双指针：
        if len(nums) <= 2:
            return len(nums)
        currPnt = 1
        pnt = 1
        count = 1 
        while pnt < len(nums):
            if nums[pnt] == nums[currPnt]:
                if count >= 2:
                    pnt += 1
                    count += 1
                else:
        # 单指针：
        # if len(nums) <= 2:
        #     return len(nums)
        # currVal = nums[0]
        # currPnt = 1
        # count = 1
        # l = 1
        # m = nums[-1]
        # while currPnt < len(nums) and nums[currPnt] >= currVal:
        #     if nums[currPnt] == currVal:
        #         if count >= 2:
        #             if nums[currPnt] == m:
        #                 break
        #             nums.pop(currPnt)
        #             nums.append(currVal)
        #             count += 1
        #         elif count < 2:
        #             currPnt += 1
        #             count += 1
        #             l += 1
        #     elif nums[currPnt] != currVal:
        #         count = 1
        #         l += 1
        #         currVal = nums[currPnt]
        #         currPnt += 1
        return l
                      
# @lc code=end
s = Solution()
l = [0,0,1,1,2,3,3,3]
s.removeDuplicates(l)
l
