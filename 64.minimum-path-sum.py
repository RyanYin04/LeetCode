#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid) -> int:
        rows = len(grid)
        columns = len(grid[0])
        if rows == 1:
            return sum(grid[0])
        if columns == 1:
            s = 0
            for i in range(rows):
                s += grid[i][0]
            return s
        
        for r in range(1, rows):
            grid[r][0] += grid[r - 1][0]
        for c in range(1, columns):
            grid[0][c] += grid[0][c - 1]
        
        for r in range(1, rows):
            for c in range(1, columns):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
        return grid[r][c]
        
# @lc code=end
s = Solution()
m = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
m = [[0]]
s.minPathSum(m)
