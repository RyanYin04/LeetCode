#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        # 使用递归的方法
        # 依次选取所有的元素作为根结点，找出[0:i]所有可能的树作为左子树
        # [i+1:]作为右子树
        if n == 0:
            return []
        def buildTree(start, end):
            trees = []

            if start > end:
                return [None]

            if start == end:
                node = TreeNode(start)
                trees.append(node)
                return trees

            elif start < end:
                for i in range(start, end +  1):
                    # 计算所有左树：
                    leftTrees = buildTree(start, i-1)
                    # 计算所有右树
                    rightTrees = buildTree(i+1, end)
                    for l in leftTrees:
                        for r in rightTrees:
                            root = TreeNode(i)
                            root.left = l
                            root.right = r
                            trees.append(root)
                return trees
        return buildTree(1,n)
        
# @lc code=end

s = Solution()
s.generateTrees(3)
len([])