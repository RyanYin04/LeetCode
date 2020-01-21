#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root) -> bool:
        def helper(root, lower, upper):
            if not root:
                return True
            val = root.val
            if val <= lower or val >= upper:
                return False
            if not helper(root.left, lower, val):
                return False
            if not helper(root.right, val, upper):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))

        # 中序遍历：
        # def inorder(root):
        #     if root == None:
        #         return []
        #     stack = []
        #     stack += inorder(root.left)
        #     stack.append(root.val)
        #     stack += inorder(root.right)
        #     return stack

        # ls = inorder(root)
        # for i in range(len(ls) - 1):
        #     if ls[i] >= ls[i + 1]:
        #         return False
        # return True
    
        
# @lc code=end

