#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        
        result = 0
        result += self.dfs(root, sum)               # 寻找一定以root为根节点的，路径和为sum的数量
        result += self.pathSum(root.left, sum)      # 寻找不一定以roor为根节点（以root.left为根节点递归），路径和为sum的数量
        result += self.pathSum(root.right, sum)     # 寻找不一定以roor为根节点（以root.left为根节点递归），路径和为sum的数量

        return result
    
    def dfs(self, root, sum):
        if root is None:
            return 0 
        
        # 由于不一定是以叶子结点为结尾，所以不需要对root.left或者root.right进行判断
        if root.val == sum:
            count = 1
        else:
            count = 0
        
        count += self.dfs(root.left, sum-root.val)
        count += self.dfs(root.right, sum-root.val)

        return count
# @lc code=end

