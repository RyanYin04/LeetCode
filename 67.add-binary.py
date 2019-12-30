#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        pnta = -1
        pntb = -1
        carry = 0
        while pnta >= -len(a) and pntb >= -len(b):
            d = int(a[pnta]) + int(b[pntb]) + carry
            if d >= 2:
                carry = 1
                d -= 2
            else:
                carry = 0
            s.insert(0, str(d))
            pnta -= 1
            pntb -= 1
        while pnta >= -len(a):
            d = int(a[pnta]) + carry
            if d >= 2:
                carry = 1
                d -= 2
            else:
                carry = 0
            s.insert(0, str(d))
            pnta -= 1
        while pntb >= -len(b):
            d = int(b[pntb]) + carry
            if d >= 2:
                carry = 1
                d -= 2
            else:
                carry = 0
            s.insert(0, str(d))
            pntb -= 1
        if carry == 1:
            s.insert(0, '1')
        return ''.join(s)
# @lc code=end

s = Solution()
s.addBinary('11', '1')