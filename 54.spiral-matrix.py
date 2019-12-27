#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        else:
            res = []
            cs = len(matrix[0]) # Number of columns.
            rs = len(matrix)    # Number of rows.
            
            # Pop the first row:
            while matrix[0][:]:
                res.append(matrix[0][0])
                matrix[0].pop(0)
            
            # Pop the last column:
            r = 1
            while r < rs:
                res.append(matrix[r][-1])
                matrix[r].pop(-1)
                r += 1
            
            # If there are only 1 column, end ethe progamme
            if cs == 1:
                return res
            
            # Pop the last row:
            while matrix[-1][:]:
                res.append(matrix[-1][-1])
                matrix[-1].pop(-1) 
            
            # Pop the fist column:
            r = rs - 2
            while r > 0 :
                res.append(matrix[r][0])
                matrix[r].pop(0)
                r -= 1

            # If there are 2 columns, programme ends here.
            # All elements in the matrix are empty lists.    
            if cs == 2:
                return res
            # Remove the first row and the last row(empty)
            matrix.pop(0)   # pop the first row
            matrix.pop(-1)  # pop the last row
            return  res + self.spiralOrder(matrix)
        
# @lc code=end

ls = [
    [1,11],
    [2,12],
    [3,13],
    [4,14],
    [5,15],
    [6,16],
    [7,17],
    [8,18],
    [9,19],
    [10,20]]

s =Solution()
s.spiralOrder(ls)