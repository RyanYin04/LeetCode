#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     # 方法1: 递归
    #     if k == 0 or head == None or head.next == None:
    #         return head
    #     temp = head
    #     l = 0
    #     while temp:
    #         l += 1
    #         temp = temp.next
    #     k = k % l
    #     lpnt = head
    #     rpnt = head.next
    #     while rpnt.next:
    #         lpnt = lpnt.next
    #         rpnt = rpnt.next
    #     rpnt.next =head
    #     lpnt.next = None
    #     return self.rotateRight(rpnt, k - 1)
        
        # 方法2: 循环
        def rotate(head):
            lpnt = head
            rpnt = head.next
            while rpnt.next:
                lpnt = lpnt.next
                rpnt = rpnt.next
            rpnt.next = head
            lpnt.next = None
            return rpnt

        if k == 0 or head == None or head.next == None:
            return head
        # 计算列表长度：
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        更新k：
        k = k % l
        开始旋转
        while k>0:
            head,l = rotate(head)
            k -= 1
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

s = Solution()
lr = s.rotateRight(l1,2);lr.val