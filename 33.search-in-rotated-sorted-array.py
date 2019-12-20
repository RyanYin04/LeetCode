#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right ) // 2
            # 必有一侧有序
            # One of the two sides must be ordered.
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < nums[right]:
                    # 右侧列表有序
                    # Right part of the list is ordered. 
                    if target > nums[mid] and target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    # 左侧列表有序
                    # Left half of the list is ordered.
                    if target >= nums[left] and target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1
# @lc code=end
s = Solution()
ls = [4,5,6,7,0,1,2]
s.search(ls,2)
