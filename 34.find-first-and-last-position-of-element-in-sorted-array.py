#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            if  nums[mid] == target:
                start = mid
                end = mid
                while nums[start] == target:
                    start -= 1
                    if start == -1:
                        break
                while nums[end] == target:
                    end += 1
                    if end == len(nums):
                        break
                return [start +1, end - 1]

        return [-1, -1]
        
        
# @lc code=end

ls = [2,3,5,7,7]
s = Solution()
s.searchRange(ls, 7)
