#
# @lc app=leetcode.cn id=95 lang=python
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.rst = []

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []

        return self.generateTree(1, n)

    # 递归的目的是找到左右子树的root节点，往root节点上挂
    # 后序遍历，错误在于搞成了先序遍历
    def generateTree(self, left, right):
        if right < left: 
            return [None]
        
        res = []
        for i in range(left, right+1):
            left_nodes = self.generateTree(left, i-1)
            right_nodes = self.generateTree(i+1, right)
            for l in left_nodes:
                for r in right_nodes:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
# @lc code=end

