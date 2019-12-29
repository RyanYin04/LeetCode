#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int):
        if n == 0:
            return []
        temp = [i for i in range(1, n**2 + 1)]
        mat = [[], for i in range(n)]
        
        c = 0
        while c <= n:
            mat[0].append(temp[0])
            temp.pop(0)
            c += 1
        
        r = 1
        while r <= n:
            mat[r]
        
# @lc code=end

