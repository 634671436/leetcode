#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is []:
            return []
        
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return
        
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
# @lc code=end

