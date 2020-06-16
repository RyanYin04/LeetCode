#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle) -> int:
        if triangle == []:
            return 0
        def helper(triangle):
            '''
            shortest path to the all the leaves
            '''
            if len(triangle) == 1:
                return triangle[0]
            elif len(triangle) > 1:
                leaf = triangle[-1]
                parentLevel = helper(triangle[:-1])
                res = [leaf[0] + parentLevel[0]]
                idx = 1
                while idx < len(leaf) - 1:
                    res.append(leaf[idx] + min(parentLevel[idx - 1], parentLevel[idx]))
                    idx += 1
                res.append(leaf[-1] + parentLevel[-1])
            return res

        paths = helper(triangle)
        return min(paths)
                

# @lc code=end

s = Solution()
ls = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
s.minimumTotal(ls)
        