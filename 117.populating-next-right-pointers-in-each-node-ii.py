#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
        def levelOrder(root, level, levels):
            if not root:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(root)
            if root.left:
                levelOrder(root.left, level + 1, levels)
            if root.right:
                levelOrder(root.right, level + 1, levels)
        levels = []
        levelOrder(root, 0, levels)
        
        for l in levels:
            idx = 0
            while idx < len(l) - 1:
                l[idx].next = l[idx + 1]
                idx += 1
        return root

# @lc code=end

