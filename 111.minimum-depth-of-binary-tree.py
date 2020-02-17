#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lheight = self.minDepth(root.left)
        rheight = self.minDepth(root.right)

        if lheight == 0 or rheight == 0:
            return 1 + lheight + rheight
            
        return min(lheight, rheight) + 1

     
        
# @lc code=end

