#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        self.res = []
        trace = []
        self.dfs(root, trace)
        
        result = []
        for item in self.res:
            result.append('->'.join(map(str, item)))

        return result
    
    def dfs(self, root, trace):
        if root is None:
            return
        
        trace.append(root.val)
        if root.left is None  and root.right is None:
            self.res.append(list(trace))

        if root.left:
            self.dfs(root.left, trace)
        if root.right:
            self.dfs(root.right, trace)
        
        trace.pop()

# @lc code=end

