#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        rs = len(matrix)
        cs = len(matrix[0])
        rlabel = 1
        clabel = 1
        for i in range(cs):
            if matrix[0][i] == 0:
                rlabel = 0
                break
        for i in range(rs):
            if matrix[i][0] == 0:
                clabel = 0
                break
        for r in range(1,rs):
            for c in range(1, cs):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, rs):
            for c in range(1,cs):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if rlabel == 0:
            for i in range(cs):
                matrix[0][i] = 0
        if clabel == 0:
            for i in range(rs):
                matrix[i][0] = 0
        return None
        
# @lc code=end

m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s = Solution()
s.setZeroes(m)
m