#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        # 后序遍历
        self.res = float("-inf")
        self.getMax(root)
        return self.res
    
    def getMax(self, root):
        if root is None:
            return 0 
        
        left = max(0, self.getMax(root.left))
        right = max(0, self.getMax(root.right))
        
        # 每计算一次值都更新最大值
        self.res = max(self.res, left + right + root.val)
        
        # 往父节点回溯的时候，不能两个节点同时返回，因此只能返回一边
        return max(left, right) + root.val

# @lc code=end

