#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        # 递归：
        if not root:
            return []
        res = []
        def helper(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        helper(root, 0)
        return res
        
        # 迭代：
        # if root == None:
        #     return []
        # res = []
        # queue = [root]
        # child = []
        # temp = []
        # while queue:
        #     node = queue.pop(0)
        #     if node:
        #         temp.append(node.val)
        #         for i in [node.left, node.right]:
        #             if i:
        #                 child.append(i)
        #     if not queue:
        #         res.append(temp)
        #         temp = []
        #         queue += child
        #         child = []
        # return res


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
s.levelOrder(t1)

