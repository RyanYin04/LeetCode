#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 初始化列表：
        nums = [i for i in range(1, n + 1)]
        res = ''
        if n == 0:
            return ''

        # 定义阶乘函数：
        def fac(num):
            if num <= 1:
                return 1
            else:
                return num * fac(num - 1)

        # 生成字符串：
        while nums:
            # 当前位置每个字符能生成的组合个数：
            np = fac(len(nums) - 1)
            # 确定该位数字：
            temp = k // np + (0 if k%np==0 else 1)
            # 添加字符
            res += str(nums[temp - 1])
            # 剔除对应元素：
            nums.pop(temp - 1)
            # 更新待满足的组合数：
            k -= np * temp
        
        return res 
# @lc code=end

s = Solution()
s.getPermutation(4,9)