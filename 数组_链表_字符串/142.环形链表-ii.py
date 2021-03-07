#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        slow, fast = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 找到之后就进行处理
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next

                return slow
                
        return None 
        
# @lc code=end

