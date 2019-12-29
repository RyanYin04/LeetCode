#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ls = s.split()
        try: 
            len(ls[-1])
            return len(ls[-1])
        except:
            return 0
# @lc code=end
def lengthOfLastWord(s):
    if s == '':
        return 0
    l = len(s) - 1
    res = 0
    while l >= 0:
        if s[l] != ' ':
            res += 1
            l -= 1
        elif s[l] == ' ':
            break
    return res

lengthOfLastWord('abcd')