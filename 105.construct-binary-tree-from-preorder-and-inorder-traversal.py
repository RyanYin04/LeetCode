#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        inorder.pop(inorder.index(preorder[0])
        preorder.pop(0)
        
        if 
        
        
# @lc code=end

