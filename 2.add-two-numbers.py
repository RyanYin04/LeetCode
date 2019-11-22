#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.22%)
# Likes:    6405
# Dislikes: 1672
# Total Accepted:    1.1M
# Total Submissions: 3.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        pnt = head
        carry = 0
        while True:
            temp = l1.val + l2.val +carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp = temp % 10
            # Update pointer value:
            pnt.val = temp
            #Update l1 and l2:
            l1 = l1.next
            l2 = l2.next
            if l1 != None and l2 != None:
                pnt.next = ListNode(None)
                pnt = pnt.next
            elif l1 == None or l2 == None:
                break
            
        while l1 != None:
            temp = l1.val + carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp = temp%10
            pnt.next = ListNode(temp)
            pnt = pnt.next
            l1 = l1.next

        while l2 != None:
            temp = l2.val + carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp = temp%10
            pnt.next = ListNode(temp)
            pnt = pnt.next
            l2 = l2.next
        
        while carry != 0:
            pnt.next = ListNode(1)
            carry = 0

        return head


