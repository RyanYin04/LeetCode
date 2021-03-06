#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        intMap = {
                    1: 'I', 4: 'IV', 5:'V', 9:'IX',
                    10: 'X', 40:'XL', 50: 'L', 90:'XC',
                    100: 'C', 400: 'CD', 500: 'D', 900:'CM',
                    1000: 'M'
                    }

        roman = ''
        keys = list(intMap.keys())
        for i in range(len(keys) - 1, -1, -1):
            roman += intMap[keys[i]] * (num // keys[i])
            num -=  (num // keys[i]) * keys[i]       
        return roman

# @lc code=end

