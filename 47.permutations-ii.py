#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        l = len(nums)
        def helpfun(ls, path, l, result):
            if len(path) == l:
                result.append(path)
                return None
            else:
                used = []
                for i in range(len(ls)):
                    if ls[i] not in used:
                        used.append(ls[i])
                        helpfun((ls[:i] + ls[i+1:]), path + [ls[i]], l, result)
                    else:
                        continue
        helpfun(nums, [], l, result)
        return result                

        
# @lc code=end

s = Solution()
s.permuteUnique([1,1,1])