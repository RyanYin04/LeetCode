#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        else:
            idx = -1
            while nums[idx] <= nums[idx - 1]:
                idx = idx - 1
                if idx == -len(nums):
                    nums.sort()
                    return None
            pivot = nums[idx - 1]
            pivotIdx = idx - 1
            while pivot < nums[idx] and idx <= -1:
                idx += 1
            nums[pivotIdx], nums[idx - 1] = nums[idx - 1], nums[pivotIdx]
            temp = sorted(nums[pivotIdx+1:])
            nums[pivotIdx+1:] = temp 
            return None

# @lc code=end
ls = [5,1,1]
s = Solution()
s.nextPermutation(ls)
ls