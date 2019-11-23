#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        The basic idea is that initialize a list to save the longest string so far. 
        
        And by traversing the whole string, if the character is not in the list, then append it to the end of list.
        
        If the character already exists
        1. Comapre the length of the current list to the max length so far.
        2. Find the position of the existing element 
        3. Reset the start of the list to be the that position and append the new element.
        
        When the traversion is done, calculate the length of the final list again and compare it 
        to the max length so far.
        '''
        max_len = 0 # The max length
        head = 0    # The index of element that is duplicate which will be treated as the head index of the new list.
        ls = []     # The list restore the substring.
        for ss in s:
            if ss not in ls:
                ls.append(ss)
            elif ss in ls:
                temp = len(ls)
                if temp > max_len:
                    max_len = temp 
                head = ls.index(ss)
                ls = ls[head+1:]
                ls.append(ss)  

        temp = len(ls)
        if temp > max_len:
            max_len = temp
        return max_len
                

        
        
