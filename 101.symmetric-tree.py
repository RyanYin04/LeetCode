#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def helper(t1, t2):
            if t1 == None or t2 == None:
                if t1 == t2:
                    return True
                else:
                    return False
            else:
                return (t1.val == t2.val and helper(t1.right, t2.left) and helper(t1.left, t2.right))
        return helper(root, root)


        
# @lc code=end
        
