#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        half_list = slow
        # 翻转链表
        last = self.reverseLinkList(half_list)

        # 翻转之后的链表长度为准
        while last:
            if last.val != head.val:
                return False
            last = last.next
            head = head.next
        
        return True

    # 翻转链表
    def reverseLinkList(self, head):

        if not head or not head.next:
            return head
        
        last = None
        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        
        return last

# @lc code=end

