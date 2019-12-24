#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i in matrix:
            temp.append(i.copy())
        size = len(matrix)
        for i in range(size):
            for j in range(size):
                print(i, j)
                matrix[j][size - 1 - i] = temp[i][j]
        return matrix        

        
# @lc code=end

