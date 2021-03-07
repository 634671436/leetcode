#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        '''
        self.max_ = 0
        # 计算以每个节点为root节点时的最大直径/考虑经不经过根节点的比较
        if root is None:
            return 0
        self.maxLength(root)
        return self.max_

    def maxLength(self, root):
        if root is None:
            return 0 
        left = self.maxLength(root.left)            # 记录当前节点root，左子树最大深度
        right = self.maxLength(root.right)          # 记录当前节点root，右子树最大深度    
        self.max_ = max(self.max_, left + right)    # 记录当前节点root，的最大直径
        return max(left, right) + 1                 # 将当前节点的最大深度返回给上一层, 作为递归只能返回一边的值
        '''

        # 考虑过不过最大直径经不经过root节点的情况
        if root is None:
            return 0 
        res = self.maxDepth(root.left) + self.maxDepth(root.right)  # 经过root节点的最大直径
        # 经过root.left or root.right节点的最大直径
        return max(res, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))

    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# @lc code=end

