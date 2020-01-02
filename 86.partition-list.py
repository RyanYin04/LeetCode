#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def partition(self, head, x: int):
        if head == None:
            return head
        pnt = head
        s = ListNode(x)
        l = ListNode(x)
        ss = s
        ll = l
        while pnt:
            if pnt.val < x:
                ss.next = pnt
                ss = ss.next
            else:
                ll.next = pnt
                ll = ll.next
            pnt = pnt.next
        ss.next = l.next
        ll.next = None
        return s.next

             
# @lc code=end
l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
s = Solution()
l = s.partition(l1, 3)
while l:
    print(l.val)
    l = l.next