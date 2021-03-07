#
# @lc app=leetcode.cn id=129 lang=python
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.res = []
        trace = []
        self.dfs(root, trace)

        return sum([int(val) for val in self.res])

    def dfs(self, root, trace):
        if root is None:
            return
        
        trace.append(root.val)
        if root.left is None and root.right is None:
            self.res.append(''.join(map(str, list(trace))))

        if root.left:
            self.dfs(root.left, trace)
        if root.right:
            self.dfs(root.right, trace)
        
        trace.pop()
# @lc code=end

