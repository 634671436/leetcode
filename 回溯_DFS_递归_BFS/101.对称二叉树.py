#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetricab(root.left, root.right)
    
    def isSymmetricab(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.isSymmetricab(left.left, right.right) and self.isSymmetricab(left.right, right.left)


# @lc code=end

