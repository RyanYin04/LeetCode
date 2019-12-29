#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        for interval in intervals:
            if interval[0] <= merged[-1][1]:
                merged[-1][-1] = max(interval[1], merged[-1][1])
            else:
                merged.append(interval)
        return merged

        
        
# @lc code=end

ls = [[1,4],[4,5]]
s = Solution()
s.merge(ls)