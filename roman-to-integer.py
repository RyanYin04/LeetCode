'''
This is the reverse function of problem 12.
This function reverse the roman number to integer.
'''

class Solution:
    def romanToInt(self, num: int) -> str:
        symbol = {'I':1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        
        keys = symbol.keys()
        val = symbol[num[-1]]
        
        for i in range(len(num) - 2, -1, -1):
            temp =  symbol[num[i]]
            if symbol[num[i +1]] > temp:
                temp = -temp
            val += temp
        return val

s = Solution()
s.romanToInt('LVIII')