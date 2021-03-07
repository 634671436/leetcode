#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        res = []
        nodes = [root]
        while nodes:
            tmp = []

            for i in range(len(nodes)):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                
                tmp.append(node.val)
            res.append(tmp[-1])

        return res
# @lc code=end

