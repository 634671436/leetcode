#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        tail = dummy
        for i in range(k):
            tail = tail.next
            # 如果是最后的节点，则直接返回
            if tail is None:
                return head
    
        # tail节点后的一个节点，也是下一次递归的起始节点
        new_head = tail.next
        head, tail = self.reverseLinkList(head, tail)
        tail.next = self.reverseKGroup(new_head, k)
        return head

    # 翻转以head为头结点，tail为尾结点的链表
    def reverseLinkList(self, head, tail):
        
        lastNode = None
        # 重点
        pHead = head
        while lastNode != tail:
            tmp = pHead.next
            pHead.next = lastNode
            lastNode = pHead
            pHead = tmp
        
        # 注意这里返回head，而不是pHead。因为此时head指向最后一个元素，而pHead和tmp都指向None
        return lastNode, head

# @lc code=end

