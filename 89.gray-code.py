#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int):
        def helpfun(n):
            if n == 0:
                return ['0']
            if n == 1:
                return ['0', '1']
            if n == 2:
                return ['00', '01', '11', '10']
            temp = helpfun(n - 1)
            return ['0' + i for i in temp] + ['1' + i for i in temp[::-1]]
        # 上下镜射
        return [int(i, 2) for i in helpfun(n)]
        

        #
        #  res = []
        # path = ''
        # def callBack(path, n, res):
        #     if len(path) == n:
        #         res.append(int(path, 2))
        #         return
        #     else:
        #         callBack(path +'0', n, res)
        #         callBack(path +'1', n, res)
        # callBack('', n, res)
        # return res
        
# @lc code=end
s = Solution()
s.grayCode(2)