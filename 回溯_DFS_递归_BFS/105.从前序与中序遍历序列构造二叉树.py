#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 边界问题的处理, 判断inorder为空
        if preorder==[] or inorder==[]:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        
        root_index = inorder.index(root_val)
        preorder_left_nodes = preorder[1:root_index+1]
        preorder_right_nodes = preorder[root_index+1:]
        inorder_left_nodes = inorder[:root_index]
        inorder_right_nodes = inorder[root_index+1:]

        root.left = self.buildTree(preorder_left_nodes, inorder_left_nodes)
        root.right = self.buildTree(preorder_right_nodes, inorder_right_nodes)
        
        return root
# @lc code=end

