#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 由于节点只能间隔rob，因此可以考虑对root的打劫情况分析：
        # 1. 如果打劫root节点，那么root.left和root.right不能打劫了;
        # 2. 如果不打劫root节点，那么它的左右子节点它也可以选择打或者不打，其收益为：
            #  max(no_steal_left, steal_left) + max(no_steal_right, steal_right)
        
        # 后序遍历
        steal, no_steal = self.dfs(root)
        return max(steal, no_steal)

    def dfs(self, root):
        if root is None:
            return (0, 0)

        steal_left, no_steal_left = self.dfs(root.left)
        steal_right, no_steal_right = self.dfs(root.right)
        
        steal = root.val + no_steal_left + no_steal_right
        no_steal = max(steal_left, no_steal_left) + max(steal_right, no_steal_right)
        
        return steal, no_steal


# @lc code=end

