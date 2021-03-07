#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head is None or head.next is None or left==right:
            return head
        
        dummy = ListNode(-1, head)
        # start为翻转链表前的一个节点
        start = dummy
        for i in range(left-1):
            start = start.next

        # 翻转链表
        pHead = start.next
        lastNode = None
        for i in range(right-left+1):
            tmp = pHead.next
            pHead.next = lastNode
            lastNode = pHead
            pHead = tmp
        
        # 将翻转的链表挂在前一个节点上
        start.next = lastNode

        # 逐个循环找到lastNode的结尾，在拼接
        while lastNode.next:
           lastNode = lastNode.next
        lastNode.next = pHead
        
        return dummy.next
# @lc code=end

