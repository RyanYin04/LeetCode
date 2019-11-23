#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0   # The index of nums1
        j = 0   # The index of nums2
        k = -1   # The index of the merged list
        ls = []
        l1 = len(nums1)
        l2 = len(nums2)
        mid = (l1 + l2) //2
        judge = (l1 + l2) % 2 == 1

        while i < l1 and j < l2 and k < mid:
            if k == mid:
                if judge:
                    return ls[k]
                else:
                    return (ls[k] + ls[k-1]) / 2
            
            elif nums1[i] <= nums2[j]:
                ls.append(nums1[i])
                i += 1
            else:
                ls.append(nums2[j])
                j += 1
            
            k += 1 
        
        while i < l1 and k < mid:
            if k == mid:
                if judge:
                    return ls[k]
                else:
                    return (ls[k] + ls[k-1]) / 2
            ls.append(nums1[i])
            i += 1
            k += 1
        
        while j < l2 and k < mid:
            if k == mid:
                if judge:
                    return ls[k]
                else:
                    return (ls[k] + ls[k-1]) /2
            ls.append(nums2[j])
            j += 1
            k += 1
        
        if k == mid:
            if judge:
                return ls[k]
            else:
                return (ls[k] + ls[k-1]) /2

            

        
# @lc code=end
s = Solution()
num1 = []
num2 = [1]
s.findMedianSortedArrays(num1, num2)