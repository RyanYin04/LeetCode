#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        upper = self.generate(numRows - 1)
        # print(upper)
        currentLevel = [1] + [upper[-1][i]+ upper[-1][i+1] for i in range(numRows - 2)] + [1]
        upper.append(currentLevel)
        return upper
        
# @lc code=end

