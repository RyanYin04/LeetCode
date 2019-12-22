#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            s = ''.join(board[r]).replace('.', '')
            if len(s) != len(set(s)):
                return False

        for c in range(9):
             column = [board[j][c] for j in range(9)]
             s = ''.join(column).replace('.', '')
             if len(s) != len(set(s)):
                 return False
        
        for b in range(9):
            rows = range(b//3*3, b//3 *3 +3)
            columns = range(b%3 * 3, b%3*3 + 3)
            block = [board[r][c] for r in rows for c in columns]
            s = ''.join(block).replace('.', '')
            if len(s) != len(set(s)):
                return False

        return True

        
# @lc code=end
            
[
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]
