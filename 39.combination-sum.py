#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
    
        def helpFun(ls,tempSum, target, path, res):
            if tempSum == target:
                res.append(path)
                return None 
            elif tempSum > target:
                return None
            elif tempSum < target:
                for i in range(len(ls)):
                    helpFun(ls[i:], tempSum + ls[i], target, path + [ls[i]], res)
        
        helpFun(candidates, 0, target, [], result)

        return result
    
# @lc code=end

ls = [2,3, 5]
s = Solution()
s.combinationSum(ls, 8)