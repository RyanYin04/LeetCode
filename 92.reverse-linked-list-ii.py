#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        if m >= n:
            return head
        new = ListNode(0)
        new.next = head
        currpnt = new
        pos = 0

        # Find the start point:
        while pos < m - 1:
            currpnt = currpnt.next
            pos += 1
        
        # Record the current location:
        l = currpnt
        r = l.next
        currpnt = r.next
        pos += 2

        # Start the insertion:
        while pos <= n:
            # print('pos:',pos)
            r.next = currpnt.next
            temp = l.next
            l.next = currpnt
            currpnt.next = temp
            currpnt = r.next
            pos += 1
        head = new.next
        return head
            
# @lc code=end
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
def listHead(l1):
    currpnt = l1
    while currpnt:
        print(currpnt.val)
        currpnt = currpnt.next
    print('\n')
    return
listHead(l5)

s = Solution()
l = s.reverseBetween(l5, 1,1)
listHead(l)
