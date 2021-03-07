#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # 增加哨兵节点，简化插入和删除操作
        h = ListNode(-1)
        h.next = head
        fast, slow = h, h   # 注意fast和slow的位置

        for _ in range(n+1):
            fast = fast.next
        
        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return h.next

# @lc code=end

