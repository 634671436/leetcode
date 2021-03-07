#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        l3 = ListNode(-1)
        l3.next = None
        p = l3

        while l1 and l2:
            if l1.val == l2.val:
                p.next = ListNode(l1.val)
                p = p.next
                p.next = ListNode(l2.val)
                l1 = l1.next 
                l2 = l2.next
                p = p.next
            elif l1.val > l2.val:
                p.next = ListNode(l2.val)
                l2 = l2.next
                p = p.next
            else:
                p.next = ListNode(l1.val)
                l1 = l1.next
                p = p.next
        
        if l1:
            p.next = l1

        if l2:
            p.next = l2
        
        return l3.next

# @lc code=end

