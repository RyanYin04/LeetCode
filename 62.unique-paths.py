#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 递归：
        # if m <= 0 or n <= 0:
        #     return 0 
        # if m == 1 or n == 1:
        #     return 1
        # return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        
        # 数学法：
        def fac(k):
            if k <= 1:
                return 1
            return k * fac(k-1)
        return int(fac(m +n -2) / (fac(m - 1) * fac(n - 1)))
        
        
# @lc code=end
s = Solution()
s.uniquePaths(7,3)