#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        res = []
        nodes = []
        nodes.append(root)

        j = 0
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
            if j%2 != 0:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            j += 1
        return res
# @lc code=end

