#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board, word: str) -> bool:
        if len(board) == 0:
            return False
        if len(word) == 0:
            return True
        def search(board, r, c, word):
            if board[r][c] != word[0]:
                return False
            if board[r][c] == word:
                return True
            
            # 更改为0，防止该位被多次匹配
            board[r][c] = 0
            # Search above
            if r > 0:
                if search(board, r-1,c, word[1:]):
                    return True
            # Search down:
            if r < len(board) - 1:
                if search(board, r+1,c, word[1:]):
                    return True
            # Search left:
            if c > 0:
                if search(board, r, c-1, word[1:]):
                    return True
            # Search right:
            if c < len(board[0]) - 1:
                if search(board, r, c+1, word[1:]):
                    return True
            
            # 若该位为起点不能匹配，则改回愿字符
            board[r][c] = word[0]
            return False
    
        for r in range(len(board)):
            for c in range(len(board[0])):
                if search(board,r,c,word):
                    return True
        return False
# @lc code=end
s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board = [['A','B','C','E']]
board = [
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]
]
s.exist(board, 'AAB')