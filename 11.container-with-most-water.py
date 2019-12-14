#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list) -> int:
        lpnt = 0
        rpnt = len(height) - 1
        maxVol = min(height[lpnt], height[rpnt]) * (rpnt - lpnt)
        while lpnt < rpnt:
            if height[lpnt] > height[rpnt]:
                rpnt = rpnt - 1
            else: 
                lpnt = lpnt + 1
            maxVol = max(maxVol, min(height[lpnt], height[rpnt]) *(rpnt - lpnt))
        return maxVol


# @lc code=end