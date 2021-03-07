#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
            
        res  = []
        nodes = []
        nodes.append(root)

        while nodes:
            tmp = []
            node_len = len(nodes)
            for i in range(0, node_len):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
        
        return res[::-1]

# @lc code=end

