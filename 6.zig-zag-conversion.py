#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        r = 0
        # The key point here is add a flag indicating whether the pointer is
        # going up or going down
        flag = 1
        # Initialize the list:
        # Each element in the list stands for the visualized rows.
        ls = ['' for i in range(numRows)]
        
        for ss in s:
            ls[r] += ss
            r += flag
            if r == numRows - 1 or r == 0:
                flag = -flag 
        return ''.join(ls)
            
# @lc code=end