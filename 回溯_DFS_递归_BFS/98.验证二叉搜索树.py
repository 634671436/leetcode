#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTa(root, -2**32, 2**32-1)
    
    def isValidBSTa(self, root, min_num, max_num):
        if root is None:
            return True
        if root.val <= min_num or root.val >= max_num:
            return False

        return self.isValidBSTa(root.left, min_num, root.val) and self.isValidBSTa(root.right, root.val, max_num)

# @lc code=end

