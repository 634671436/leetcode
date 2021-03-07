#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(-1)
        l3.next = None
        p = l3
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        step_falg = 0
        while l1 and l2:
            cur_val = l1.val + l2.val + step_falg
            if cur_val >= 10:
                cur_node = ListNode(cur_val%10)
                step_falg = 1
            else:
                cur_node = ListNode(cur_val)
                step_falg = 0
            p.next = cur_node
            p = p.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            cur_val = l1.val + step_falg
            if cur_val >= 10:
                cur_node = ListNode(cur_val%10)
                step_falg = 1
            else:
                cur_node = ListNode(cur_val)
                step_falg = 0
            p.next = cur_node
            p = p.next
            l1 = l1.next
        
        while l2:
            cur_val = l2.val + step_falg
            if cur_val >= 10:
                cur_node = ListNode(cur_val%10)
                step_falg = 1
            else:
                cur_node = ListNode(cur_val)
                step_falg = 0
            p.next = cur_node
            p = p.next
            l2 = l2.next
        
        if step_falg == 1:
            cur_node = ListNode(1)
            p.next = cur_node
            p = p.next
        
        return l3.next
   
# @lc code=end

