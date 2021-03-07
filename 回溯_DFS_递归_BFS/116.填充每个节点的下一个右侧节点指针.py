#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        
        nodes = [root]
        while nodes:
            
            for i in range(len(nodes)):
                if i == len(nodes) - 1:
                    nodes[i].next = None
                else:
                    nodes[i].next = nodes[i+1]
            
            # 用于将上一层加入的最新一层pop完
            for i in range(len(nodes)):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

        return root

# @lc code=end

