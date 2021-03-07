#
# @lc app=leetcode.cn id=230 lang=python
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.res = 0
        self.idx = k

        self.val = []
        self.dfs(root)
        return self.res
    
    # 递归中间无法停止，因此可以考虑用栈模型递归的过程，获取结果
    def dfs(self, root):
        if root is None:
            return

        self.dfs(root.left)
        self.val.append(root.val)
        if len(self.val) == self.idx:
            self.res = root.val
        self.dfs(root.right)        

# @lc code=end

