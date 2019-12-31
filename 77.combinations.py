#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) :
        if n == 0:
            return []
        elif k == 1:
            return [[i] for i in range(1, n + 1)]
        ls = [i for i in range(1, n +1)]
        res = []
        def callback(ls,k,path,res):
            if len(path) ==  k:
                res.append(path)
                return
            elif len(path) < k:
                for i in range(len(ls)):
                    callback(ls[i+1:], k, path+ [ls[i]], res)
        callback(ls, k, [], res)
        return res
        
        
# @lc code=end

s = Solution()
s.combine(1,1)