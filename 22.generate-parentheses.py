#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        helpFun('', 0, n, n, result)
        return result
    
def helpFun( s, balance, lres, rres, result):
    if balance > 0 and lres == 0:
        while rres > 0:
            s += ')'
            rres -= 1
        result.append(s)
    if balance > 0 and lres > 0:
        helpFun(s + '(', balance + 1, lres - 1, rres, result)
        helpFun(s + ')', balance - 1, lres, rres - 1, result)
    if balance == 0 and lres > 0:
        helpFun(s + '(', balance + 1, lres - 1, rres, result)
    

# @lc code=end
