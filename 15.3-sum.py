#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums) :
        # Sort the list:
        ls = sorted(nums)
        preVal = None
        result = []
        for i, a in enumerate(ls):
            ## 确保没有重复结果：
            ## 保证选取的最小值与上次不同
            if a == preVal:
                continue
            if a > 0:
                break
            preVal = a
            lpnt = i + 1
            rpnt = len(ls) - 1
            ## 创建双指针
            ## 指针从两侧向中间移动
            while lpnt < rpnt:
                b = ls[lpnt]
                c = ls[rpnt]
                if c < 0:
                    break
                if a + b + c == 0:
                    result.append([a,b,c])

                    ## 保证中间没有重复结果：
                    while lpnt < rpnt and ls[lpnt] == ls[lpnt + 1]:
                        lpnt += 1
                    while lpnt < rpnt and ls[rpnt] == ls[rpnt - 1]:
                        rpnt -= 1
                    lpnt += 1
                    rpnt -= 1

                if a + b +c > 0:
                    rpnt -= 1
                if a + b + c < 0:
                    lpnt += 1
        return result


        
# @lc code=end
