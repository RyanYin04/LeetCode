#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # DFS:
        if root == None:
            return 0
        else:
            levels = []
            def helper(root, level):
                if len(levels) == level:
                    levels.append([])
                if root:
                    levels[level].append(root)
                if root.left:
                    helper(root.left, level + 1)
                if root.right:
                    helper(root.right, level + 1)
            helper(root, 0)
        return len(levels)

        
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
s.maxDepth(t1)