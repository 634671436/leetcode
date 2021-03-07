#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        '''
        res = []
        nodes = []
        res.append([root.val])
        nodes.append([root])

        # 必须保证在同一层的节点在一起
        while len(nodes) > 0:
            node_lst = nodes.pop(0)
            tmp = []
            for node in node_lst:
                if node.left != None:
                    tmp.append(node.left)
                if node.right != None:
                    tmp.append(node.right)
            if len(tmp) > 0:
                nodes.append(tmp)
                res.append([item.val for item in tmp])
        '''

        res = []
        
        nodes = []
        nodes.append(root)

        while nodes:
            # 每一次循环都是当前层, 其中pop完之后，新增的节点都是下一层所有的节点
            tmp = []
            node_lst = len(nodes)
            for i in range(0, node_lst):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
        return res
# @lc code=end

