#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if (root == None) | (root.left == None and root.right == None):
            return 
        if root.left:
            ltree = self.flatten(root.left)
        if root.right:
            rtree = self.flatten(root.right)
        
        def connectTree(ltree, rtree):
            pnt = ltree
            if not rtree:
                return None
                
            while pnt.right:
                pnt = pnt.right
            pnt.right = rtree

        connectTree(ltree, rtree)
        root.right = ltree

        def traverse(root):
            pnt = root
            while pnt:
                print(pnt.val)
                pnt = pnt.right


        
# @lc code=end

