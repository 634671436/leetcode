#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left) + 1, self.depth(root.right) + 1)
# @lc code=end

