#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root) -> bool:
        self.isValid = True #注意作用域！

        def height(root):
            # 用于计算树的高度
            if not root:
                return 0
            lheight = height(root.left) + 1 #左树高度
            rheight = height(root.right) + 1 #右树高度

            if abs(lheight - rheight) > 1:
                # 判断根结点是否平衡
                self.isValid = False
            return max(lheight, rheight) #返回树高度，即左树或右树较大者
        
        height(root)
        return self.isValid 
        
# @lc code=end

a = 10

def tt(b):
    if b > 10:
        a = b
    return b > 10

tt(15)
a