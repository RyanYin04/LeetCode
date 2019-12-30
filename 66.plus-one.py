#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        digits.insert(0, 0) 
        digits[-1] += 1
        loc = -1
        while loc > -len(digits):
            if digits[loc] >= 10:
                digits[loc - 1] += 1
                digits[loc] = digits[loc] % 10
            loc -= 1
        if digits[0] == 0:
            digits.pop(0)
        return digits
        
# @lc code=end

s = Solution()
s.plusOne([9])