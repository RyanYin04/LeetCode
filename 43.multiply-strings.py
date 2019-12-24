#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        else:
            result = [0 for i in range(len(num1) + len(num2))]
            if len(num1) >= len(num2):
                lnum, snum = num1, num2
            else:
                lnum, snum  = num2, num1
            
            # 逐位相乘, 用列表存储结果
            # Mutiply by digit, and save ethe result in a list.
            for i in range(-1, -len(snum) - 1, -1):
                for j in range( -1 , -len(lnum) - 1, -1):
                    temp = int(snum[i]) * int(lnum[j])
                    result[i +j + 1] += temp
            # 处理进位
            for d in range(-1, -len(result) - 1, -1):
                if result[d] > 9:
                    result[d - 1] += result[d] // 10
                result[d] = str(result[d] % 10)
            if result[0] == '0':
                result.pop(0)
            return ''.join(result)
        return result
# @lc code=end
s = Solution()
s.multiply('382', '151')
