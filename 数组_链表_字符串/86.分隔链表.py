#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        #if head.next is None:
        #    return head
        
        '''
        fast, slow = head, head
        while fast:
            if fast.val < x:
                # 会打乱顺序，出错
                fast.val, slow.val = slow.val, fast.val
                slow = slow.next
            fast = fast.next
        '''

        # 重新创建链表，分为大小两段
        min_node = ListNode(0)
        pHead_a = min_node
        max_node = ListNode(0)
        pHead_b = max_node

        while head:
            if head.val < x:
                curnode = ListNode(head.val)
                min_node.next = curnode
                min_node = min_node.next
            else:
                curnode = ListNode(head.val)
                max_node.next = curnode
                max_node = max_node.next
            
            head = head.next
        min_node.next = pHead_b.next
        return pHead_a.next

# @lc code=end

