#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 递归：
        if head == None or head.next == None:
            return head
        curr = head.next
        if curr.val == head.val:
            while curr and curr.val == head.val:
                curr = curr.next
            head = curr
            head = self.deleteDuplicates(curr)
        else:
            head.next = self.deleteDuplicates(curr)
        return head
        
        # 循环：
        # if head == None or head.next == None:
        #     return head
        # count = 1
        # temp = head
        # while temp.next:
        #     if temp.val == temp.next.val:
        #         temp = temp.next
        #         count += 1
        #     else:
        #         if count == 1:
        #             head = temp
        #             break
        #         if count > 1:
        #             count = 1
        #             temp = temp.next
        # if temp.next == None and count >= 2:
        #     return None
        # elif temp.next and count == 1:
        #     head = temp
        # elif temp.next == None and count == 1:
        #     return temp
        # elif temp.next and count >= 2:
        #     head = temp.next
        # currPnt = head
        # pnt = head.next
        # while pnt.next:
        #     if pnt.val == pnt.next.val:
        #         pnt = pnt.next
        #         count += 1
        #     else:
        #         if count == 1:
        #             currPnt.next = pnt
        #             pnt = pnt.next
        #             currPnt = currPnt.next
        #         if count > 1:
        #             pnt = pnt.next
        #             count = 1
        # if count == 1:
        #     currPnt.next = pnt
        # else:
        #     currPnt.next = None
        # return head
# @lc code=end
l1 = ListNode(2)
l2 = ListNode(2)
# l3 = ListNode(2)
# l4 = ListNode(3)
# l5 = ListNode(4)
# l6 = ListNode(4)
# l7 = ListNode(5)
l1.next = l2
# l2.next = l3
# l3.next = l4

s = Solution()
l = s.deleteDuplicates(l1)
while l:
    print(l.val)
    l = l.next

