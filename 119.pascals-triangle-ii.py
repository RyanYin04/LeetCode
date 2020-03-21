#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        upper = self.getRow(rowIndex - 1)
        return [1] + [upper[i] + upper[i+1] for i in range(rowIndex - 1)] + [1]
# @lc code=end

