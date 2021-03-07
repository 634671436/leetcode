#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        
        if res is None:
            return None

        res.sort()
        l1 = ListNode(-1)
        l1.next = None
        p = l1
        
        #while res:
        for i in res:
            p.next = ListNode(i)
            p = p.next

        return l1.next
# @lc code=end

