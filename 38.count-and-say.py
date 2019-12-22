#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            back = self.countAndSay(n - 1)
            result = ''
            i = 0
            while i < len(back):
                count = 1
                currVal = back[i]
                while i < len(back) - 1 and back[i] == back[i +1]:
                    count += 1
                    i += 1
                i += 1
                result += str(count) + currVal
        return result
                
        
# @lc code=end

s = Solution()
s.countAndSay(25)