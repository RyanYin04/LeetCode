#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        # 卡特兰数：
        g = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(1, i+1):
                count += g[j - 1] * g[i - j]
            g.append(count)
        return g[-1]
        #  递归：
        # if n <= 1:
        #     return n
        # def allTrees(start, end):
        #     count = 0
        #     if start > end + 1:
        #         return 0
        #     elif start == end + 1:
        #         return 1
        #     elif start == end - 1:
        #         return 2
        #     else:
        #         for i in range(start, end+1):
        #             ltrees = allTrees(start, i - 1)
        #             rtrees = allTrees(i + 1, end)
        #             count += ltrees * rtrees
        #         return count
        # return allTrees(1, n)
        
# @lc code=end
s = Solution()
s.numTrees(19)
