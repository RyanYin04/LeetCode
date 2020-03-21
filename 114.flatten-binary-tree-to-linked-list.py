#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 方法一：前序遍历，保存所有节点
        # if not root:
        #     return None
        # def helper(root, res):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     if root.left:
        #         helper(root.left, res)
        #     if root.right:
        #         helper(root.right, res)
        #     return res
        # roots = helper(root, [])[1:]
        # pnt = root
        # root.left = None
        # for i in roots:
        #     pnt.right = TreeNode(i)
        #     pnt = pnt.right

        # 方法二：
        # 循环将左节点插入右节点
        pnt = root
        while pnt:
            if not pnt.left:
                pnt = pnt.right
            else:
                lnode = pnt.left
                while lnode.right:
                    lnode = lnode.right
                lnode.right = pnt.right
                pnt.right = pnt.left
                pnt.left = None
                pnt = pnt.right        
# @lc code=end

