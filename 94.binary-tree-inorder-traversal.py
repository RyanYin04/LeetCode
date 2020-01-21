#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        # 1. Loop:
        # use stack:
        curr = root
        while curr.right:
            
        # 2.Recursion:
        # ls = []
        # if root:
        #     ls += self.inorderTraversal(root.left)
        #     ls.append(root.val)
        #     ls += self.inorderTraversal(root.right)
        # return ls

        
# @lc code=end
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r1.right = r2
r2.left = r3
s = Solution()
s.inorderTraversal(r1)
