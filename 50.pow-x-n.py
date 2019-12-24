#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = 1 if n > 0 else -1 # 判断指数正负
        n = n * flag # 转化为正数
        def helpfun(x,power):
            if power == 0:
                return 1
            elif power == 1:
                return x
            else:
                if power % 2 == 1:
                    return x*helpfun(x*x, (power - 1)/ 2)
                else:
                    return helpfun(x*x, power / 2)
        return helpfun(x, n) if flag > 0 else 1 / helpfun(x,n)
        
# @lc code=end
s = Solution()
s.myPow(2.0000,10)
