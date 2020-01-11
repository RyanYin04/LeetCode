#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m * n == 0:
            nums1[:] = (nums1 * (m >0) + nums2 * (n>0))[:]
            return None
        pnt1 = 0
        pnt2 = 0
        while pnt1 < m + pnt2 and pnt2 < n:
            if nums2[pnt2] <= nums1[pnt1]:
                nums1[pnt1], nums1[pnt1 + 1: ] = nums2[pnt2], nums1[pnt1:-1]
                pnt2 += 1
                pnt1 += 1
            else:
                pnt1 += 1
        while pnt2 < n:
            nums1[pnt1] = nums2[pnt2]
            pnt1 += 1
            pnt2 += 1
        return None

        
# @lc code=end
s = Solution()
ls1 = [-1,0,0,3,3,3,0,0,0]
ls2 = [1,2,2]
s.merge(ls1, 6,ls2, 3)
ls1
# ls1*(0>0) + ls2*(3>0)