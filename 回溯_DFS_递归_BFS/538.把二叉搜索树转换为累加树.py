#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
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
        self.sum = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        
        # 累加二叉搜索树中大于当前值得val，并进行更新
        # 遍历的方式是中序遍历，但是以root.right为起始点，[8, 7, 6, 5, 4, 3, 2, 1, 0]
        #                                         root= 8, 7, 6, 5, 4, 3, 2, 1, 0
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)

        return root
# @lc code=end

