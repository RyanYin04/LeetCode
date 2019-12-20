#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val <= l2.val:
                head = l1
                currPnt = l1
                pnt1 = l1.next
                pnt2 = l2
            else:
                currPnt = l2
                head = l2
                pnt1 = l1
                pnt2 = l2.next
            while pnt1 != None and pnt2 != None:
                if pnt1.val <= pnt2.val:
                    currPnt.next = pnt1
                    currPnt = currPnt.next
                    pnt1 = pnt1.next
                else:
                    currPnt.next = pnt2
                    currPnt = currPnt.next
                    pnt2 = pnt2.next

            while pnt1 != None:
                currPnt.next = pnt1
                currPnt = currPnt.next
                pnt1 = pnt1.next
            while pnt2 != None:
                currPnt.next = pnt2
                currPnt = currPnt.next
                pnt2 = pnt2.next
        
        return head

# @lc code=end


