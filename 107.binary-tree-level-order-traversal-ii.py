#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []

        levels = []
        def helper(root, level):
            if len(levels) == level:
                levels.append([])
            if root:
                levels[level].append(root.val)
            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)

        helper(root, 0)
        return levels[::-1]

# @lc code=end
t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

s = Solution()
s.levelOrderBottom(t1)
