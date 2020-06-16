#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices) -> int:
        # 暴力法：
        # if len(prices) == 0:
        #     return 0
        # idx = 0
        # maxProfit = 0
        # while idx < len(prices) - 1:
        #     currentProfit = -prices[idx] + max(prices[idx+1:]) 
        #     currentProfit = currentProfit if currentProfit > 0 else 0
        #     maxProfit = max(maxProfit, currentProfit)
        #     # print(currentProfit, idx)
        #     idx += 1
        # return maxProfit 
        
        # 一次遍历：
        maxProfit = 0
        minPrice = float('inf')
        for i in prices:
            maxProfit = max(i - minPrice, maxProfit)
            minPrice = min(i, minPrice)
        return maxProfit
               
# @lc code=end
s = Solution()
s.maxProfit([7,1,5,3,6,4])
