#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums, target: int) -> bool:
        l = 0
        r = len(nums) - 1
        # 去重：
        # 如果左边界等于右边界，那么左边界向左移动，防止无法正确判断到底mid哪侧有序
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            # 判断有序侧：
            if nums[mid] <= nums[r]:
                # righthand side is ordered：
                if nums[mid] < target and nums[r]>=target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] == nums[r]:
                l += 1

            else:
                # lefthand side is ordered:
                if nums[mid]> target and nums[l] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False 
     
# @lc code=end
s = Solution()
s.search([3,1,1], 3)
