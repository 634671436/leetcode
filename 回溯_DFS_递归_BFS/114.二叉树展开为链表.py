#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return []
        
        self.trace = []
        self.dfs(root)

        for i in range(len(self.trace)):
            if i == len(self.trace)-1:
                self.trace[i].right = None
                self.trace[i].left = None
            else:
                self.trace[i].right = self.trace[i+1]
                self.trace[i].left = None
        
        return self.trace[0]
    
    def dfs(self, root):
        if root is None:
            return 
        
        # 回溯的过程依赖本身递归完成，而trace只是记录了过程而已，因此这里不需要用pop来记录过程
        self.trace.append(root)
        self.dfs(root.left)
        self.dfs(root.right)

# @lc code=end

