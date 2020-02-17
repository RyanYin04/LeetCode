#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s):
        if not root:
            return []
        res = []

        def callBack(root, path, tempSum):
            if root.left == None and root.right == None:
                if tempSum + root.val == s:
                    res.append(path + [root.val])
            if root.left:
                callBack(root.left, path + [root.val], tempSum + root.val)
            if root.right:
                callBack(root.right, path + [root.val], tempSum + root.val)
        
        callBack(root, [], 0)

        return res
        
# @lc code=end

