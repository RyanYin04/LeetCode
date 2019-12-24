#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums):
        result = []
        nums.sort()
        def helpFun(ls, path, res, l):
            if len(path) == l:
                res.append(path)
                return None
            else:
                for i in range(len(ls)):
                    helpFun(ls[:i] + ls[(i + 1):], path + [ls[i]], res, l)
        helpFun(nums, [], result, len(nums))
        return result
# @lc code=end

s = Solution()
len(s.permute([1,2,3,4]))