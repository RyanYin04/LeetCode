#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 方法一：
        # Level order 遍历，保存所有节点，并连接
        # if not root:
        #     return None
        # levels = []
        # def helper(root, levels, level):
        #     if not root:
        #         return 
        #     if len(levels) == level:
        #         levels.append([])
        #     levels[level].append(root)
        #     helper(root.left, levels, level + 1)
        #     helper(root.right, levels, level+1)
        # helper(root, levels, 0)
        # for l in levels:
        #     if len(l) > 1:
        #         i = 0
        #         while i < len(l) - 1:
        #             l[i].next = l[i + 1]
        #             i += 1              
        # return root

        # Follow Up：O(1) space complexity
        if not root:
            return None
        if root.left and root.right:
            root.left.next = root.right
            self.connect(root.left)
            self.connect(root.right)
        if root.next:
            root.right.next = root.next.left
        return root

# @lc code=end

