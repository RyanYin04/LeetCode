#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        # 遍历第一行：
        for c in range(1, columns):
            if obstacleGrid[0][c] == 1 or obstacleGrid[0][c - 1] == 0:
                obstacleGrid[0][c] = 0
            else:
                obstacleGrid[0][c] = 1
        
        # 遍历第一列：
        for r in range(1, rows):
            if obstacleGrid[r][0] == 1 or obstacleGrid[r - 1][0] == 0:
                obstacleGrid[r][0] = 0
            else:
                obstacleGrid[r][0] = 1
        
        # 按列-行遍历所有剩余位置：
        for r in range(1, rows):
            for c in range(1, columns):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
        return obstacleGrid[rows - 1][columns - 1]

        
# @lc code=end
s = Solution()
s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
