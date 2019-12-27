#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        # 扫描法：
        # 从列表第一个元素开始遍历
        # 分别保存至此最大值（maxval）和以该元素为终点的列表的值（res）
        # 如果res<0, 那么该部分的值对于后边列表的总和增大没有帮助， 重置res
        # maxval = max(maxval, res)
        if len(nums) == 1:
            return nums[0]
        else:
            i = 1
            curr = nums[0]
            maxval = nums[0]
            while i < len(nums):
                if curr < 0:
                    curr = nums[i]
                else:
                    curr += nums[i]
                maxval = max(curr, maxval)
                i+= 1
            return maxval
        
# @lc code=end
def maxSubArray(nums):
    # 动态规划：
    # 定义sum[i]为： 以i为结点的最长字符串的和
    # 以nums[i]为结尾的最大子序列和只能是以下两种情况之一：
    # 1. 如果以nums[i-1]为结尾的最大和子序列>0: sum[i] = sum[i - 1] + nums[i]
    # 2. 如果以nums[i-1]为结尾的最大和子序列<0: sum[i] = nums[i]
    # -> 状态转移方程为：sum[i] = max(sum[i - 1] + nums[i], nums[i])
    maxval = nums[0]
    sums = nums[0]
    for i in range(len(nums)):
        if sums <= 0:
            sums = nums[i]
        else: 
            sums = sums + nums[i]
        maxval = max(sums, maxval)
    return maxval



s = Solution()
s.maxSubArray([-2,-1,3,9,-9, 15,-3,20])

maxSubArray([-2,-1,3,9,-9, 15,-3,20])