#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 先分别求headA和headB的长度，再求得差值，让长一点的链表先走一段距离
        if headA is None or headB is None:
            return None
        
        len_a, len_b = 0, 0
        tmp_a, tmp_b = headA, headB
        while tmp_a:
            len_a += 1
            tmp_a = tmp_a.next
        
        while tmp_b:
            len_b += 1
            tmp_b = tmp_b.next

        if len_a > len_b:
            len_diff = len_a - len_b
            while len_diff > 0:
                headA = headA.next
                len_diff -= 1
        else:
            len_diff = len_b - len_a
            while len_diff > 0:
                headB = headB.next
                len_diff -= 1
        
        while headA and headB:
            if headA != headB:
                headA, headB = headA.next, headB.next
            else:
                return headA
        
        return None
# @lc code=end

