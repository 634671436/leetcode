#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        self.result = []
        # 路径
        track = []
        self.pathSum_record(root, targetSum, track)
        return self.result

    def pathSum_record(self, root, targetSum, track):
        
        if root is None:
            return
        
        track.append(root.val)
        # 满足条件，增加路径到最后结果
        if root.left is None and root.right is None and root.val == targetSum:
            self.result.append(list(track))
        
        # root.left and root.right 就是选择
        self.pathSum_record(root.left, targetSum-root.val, track)
        self.pathSum_record(root.right, targetSum-root.val, track)
        track.pop()
        

# @lc code=end

