#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if k == 0:
            return head

        length = 1
        tail = head
        while tail != None and tail.next != None:
            tail = tail.next
            length += 1
        
        # 变成循环链表
        tail.next = head
        
        new_k = k % length
        if length == 0:
            return head

        # tail节点移动的步数，找到此时链表真正的尾结点。重点是length-new_k
        for i in range(length-new_k):
            tail = tail.next
        
        new_head = tail.next
        tail.next = None

        return new_head


# @lc code=end

