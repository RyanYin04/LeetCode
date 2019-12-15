#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    # Method I: Using the max & min of the strings and make comparison between
    # these 2.
    # def longestCommonPrefix(self, strs: list) -> str:
    #     if len(strs) == 0:
    #         return ''
            
    #     lprf = ''
    #     maxStr = max(strs)
    #     minStr = min(strs)
    #     for i, s in enumerate(minStr):
    #         if s == maxStr[i]:
    #             lprf += s
    #         else: 
    #             break
    #     return lprf

    # Method II: Using 
    def longestCommonPrefix(self, ls:list) -> str:
        lprf = ''
        l = len(ls)
        if l == 0:
            return lprf
        for i, ss in enumerate(ls[0]):
            flag = 1
            for j in ls[1:]:
                if i > len(j) - 1 or ss != j[i]:
                    flag = -1
                    break
            if flag == 1:
                lprf = lprf + ss
            if flag == -1:
                break
        return lprf
