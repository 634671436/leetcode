#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """        
        # 利用先序和中序会超时
        #self.preorder = []
        #self.inorder = []

        #self.search(root)
        #res = self.res(p, q, self.preorder, self.inorder)
        
        # return res
        # 分治法思想
        if root is None or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root   # 若在左子树中找到p, 右子树中找到q，则就是root
        if left is None:
            return right
        if right is None:
            return left
        
        return None
        
    
    def res(self, p, q, preorder, inorder):
        
        if preorder==[] or inorder==[]:
            return

        root_idx = inorder.index(preorder[0])
        if inorder.index(p) < root_idx and inorder.index(q) < root_idx:
            return self.res(p, q, preorder[1:root_idx+1], inorder[:root_idx])
        if inorder.index(p) > root_idx and inorder.index(q) > root_idx:
            return self.res(p, q, preorder[root_idx+1:], inorder[root_idx+1:])

        return preorder[0]

    def search(self, root):
        # 递归的本质就是在寻找当前节点的下一次选择
        self.p_dfs(root)
        self.i_dfs(root)

    def p_dfs(self, root):
        if root is None:
            return

        self.preorder.append(root)
        self.p_dfs(root.left)
        self.p_dfs(root.right)
    
    def i_dfs(self, root):
        if root is None:
            return

        self.i_dfs(root.left)
        self.inorder.append(root)
        self.i_dfs(root.right)
        
# @lc code=end

