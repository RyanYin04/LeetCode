#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, s) -> bool:
        # 方法一：
        # 回溯法：
        # 记录所有路径和，最后判断目标值是否存在于该列表
        # if root == None:
        #     return False
        # res = []
        # def callBack(root,path, res):
        #     if root.left:
        #         callBack(root.left, path + root.val, res)
        #     if root.right:
        #         callBack(root.right, path + root.val, res)
        #     if root.right == None and root.left == None:
        #         res.append(path + root.val)
        #     return None
        # callBack(root, 0, res)
        # return (s in res)            
        # 

        # 方法二：
        # 直接递归+截断：
        
        if not root:
            return False
        if (root.right == None) & (root.left == None):
            return root.val == s
        return (self.hasPathSum(root.left, s - root.val)) | (self.hasPathSum(root.right, s - root.val))
        
    
# @lc code=end

