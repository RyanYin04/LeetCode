#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        ## Use stack. Every time is a match, pop it out of the stack.
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0 
        
# @lc code=end

