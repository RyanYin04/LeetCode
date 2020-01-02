#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        currPnt = head
        pnt = currPnt.next
        while pnt:
            if pnt.val != currPnt.val:
                currPnt.next = pnt
                currPnt = currPnt.next
            pnt = pnt.next
        currPnt.next = None
        return head   
# @lc code=end

