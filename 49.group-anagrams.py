#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs):
        temp = [''.join(sorted(i)) for i in strs]
        dic = {}
        for i in range(len(temp)):
            if temp[i] not in dic:
                dic[temp[i]] = [strs[i]]
            else:
                dic[temp[i]].append(strs[i])
        return list(dic.values())

        
# @lc code=end
ls = ["eat", "tea", "tan", "ate", "nat", "bat"]
s =Solution()
s.groupAnagrams(ls)