#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums,  val: int) -> int:
        D = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                D += 1
            else:
                nums[i - D] = nums[i]
            i += 1 
        return (len(nums) - D)
            
        
# @lc code=end
s = Solution()
ls = [0,1,2,2,3,0,4,2]
s.removeElement(ls, 2)
ls
