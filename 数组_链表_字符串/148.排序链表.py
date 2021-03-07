#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 归并排序，一直递归到最下层。
        # 思想：先把左右两边都排好序，再合并
        if head is None or head.next is None:
            return head
        
        mid = self.getMid(head)
        # 传入引用，对head进行了修改
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.mergeTwoLists(left, right)
    

    def getMid(self, head):
        
        if head is None or head.next is None:
            return head
        
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None
        return slow

    def mergeTwoLists(self, l1, l2):
        
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

