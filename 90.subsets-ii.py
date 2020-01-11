#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        def callBack(ls, path, res):
            res.append(path)
            i = 1
            for i in range(len(ls)):
                if i > 0 and ls[i] == ls[i - 1]:
                    continue
                callBack(ls[i+1:], path +[ls[i]], res)
        res = []
        callBack(nums, [],res)
        return res
# @lc code=end
s = Solution()
s.subsetsWithDup([1,2,2,3])
