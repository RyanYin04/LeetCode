#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        ls = [1, 2]
        for i in range(2, n):
            ls.append(ls[i - 1] + ls[i - 2])
        return ls[-1]
        # 递归：
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n-2)
        
# @lc code=end

s = Solution()
s.climbStairs(4)