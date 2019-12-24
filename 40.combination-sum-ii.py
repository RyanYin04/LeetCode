#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        result = []
        def helpFun(ls, path, result, tempSum, target):
            if tempSum == target:
                result.append(path)
                return None
            elif tempSum > target:
                return None
            elif tempSum < target:
                i = 0
                while i < len(ls):
                    if i > 0 and ls[i] == ls[i - 1]:
                        i += 1
                    else:
                        helpFun(ls[i+1:], path + [ls[i]], result, tempSum + ls[i], target)
                        i += 1
        helpFun(candidates, [], result, 0, target)
        return result
        
        
# @lc code=end

s = Solution()
ls = [2,5,2,1,2]
s.combinationSum2(ls, 5)