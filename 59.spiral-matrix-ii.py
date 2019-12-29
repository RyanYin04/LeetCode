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
        # Initialize the matrix:
        mat = [[0] * n for i in range(n)]
        # Start the filling process:
        round = n//2 + n%2
        i = 0
        num = 1
        while i <= round - 1:
            # direction: Going right
            c = i
            while c < n - i:
                mat[i][c] = num
                num += 1
                c += 1
            
            # direction: Going down
            r = i + 1
            while r < n - i:
                mat[r][-i - 1] = num
                num += 1
                r += 1

            # Direction: Going left
            c = n - i - 2
            while c >= i:
                mat[-i - 1][c] = num
                num += 1
                c -= 1

            # Direction: Going up
            r = n - i - 2
            while r > i:
                mat[r][i] = num
                num += 1
                r -= 1

            i += 1
        return mat            



        
# @lc code=end

