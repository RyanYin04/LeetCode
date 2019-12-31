#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        # 回溯法：
        nums.sort()
        if nums == []:
            return []
        # elif len(nums) == 1:
        #     return [nums]+[[]]
        res = []
        def callback(ls, path, res):
            if ls == []:
                return
            for i in range(len(ls)):
                res.append(path + [ls[i]])
                callback(ls[i+1:], path+[ls[i]], res)
        callback(nums, [], res)
        res.append([])
        return res
        
# @lc code=end
s = Solution()
s.subsets([0])
