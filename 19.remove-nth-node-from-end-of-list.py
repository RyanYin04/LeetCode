#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = head
        lpnt = head
        rpnt = head
        r = 0
        while r < n:
            r += 1
            rpnt = rpnt.next
        if rpnt == None:
            return start.next
        else:
            while rpnt.next != None:
                rpnt = rpnt.next
                lpnt = lpnt.next
            temp = lpnt.next.next
            lpnt.next = temp
        return start 
# @lc code=end

