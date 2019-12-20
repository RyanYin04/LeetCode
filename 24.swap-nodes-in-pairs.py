#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Method I: Double pointer:

    # def swapPairs(self, head: ListNode) -> ListNode:
    #     if head == None or head.next == None:
    #         return head
    #     else:
    #         pnt1 = head
    #         pnt2 = head.next
    #         while True:
    #             tempVal = pnt1.val
    #             pnt1.val, pnt2.val = pnt2.val, pnt1.val
    #             pnt1 = pnt2.next
    #             if pnt1 == None:
    #                 return head
    #             else:
    #                 pnt2 = pnt1.next
    #                 if pnt2 == None:
    #                     return head
    
    # Method II: Recursion
    
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        else:
            head.val, head.next.val = head.next.val, head.val
            self.swapPairs(head.next.next)
            return head
        
# @lc code=end

