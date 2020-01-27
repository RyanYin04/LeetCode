#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) :
        # # 遍历：
        # if not root:
        #     return []
        # queue = [root]
        # child = []
        # res = []
        # level = []
        # while queue:
        #     node = queue[0]
        #     queue.pop(0)
        #     level.append(node.val)
        #     if len(res)%2 == 1:
        #         for i in [node.left, node.right]:
        #             if i:
        #                 child.append(i)
        #     elif len(res) % 2 == 0:
        #         for i in [node.left, node.right]:
        #             if i:
        #                 child.insert(0, i)
        #     if not queue:
        #         res.append(level)
        #         queue += child
        #         child = []
        #         level = []
        # return res

                

        # 递归：
        if not root:
            return []
        res = []
        def helper(root, level):
            if len(res) == level:
                res.append([])
            if level % 2 == 1:
                res[level].insert(0, root.val)
            elif level % 2 == 0:
                res[level].append(root.val)
            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)
        helper(root, 0)

        return res
        
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
s.zigzagLevelOrder(t1)

