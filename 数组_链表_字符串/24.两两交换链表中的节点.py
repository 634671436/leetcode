#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 增加哑结点
        pHead = ListNode(-1)
        pHead.next = head

        dummy = pHead
        while pHead.next and pHead.next.next:
            slow, fast = pHead.next, pHead.next.next
            pHead.next = fast           # 把前面的节点直接挂到pHead上
            slow.next = fast.next       # 把前面节点的next串挂载到slow节点上
            fast.next = slow            # 把slow节点挂载到fast.next上，串起来

            pHead = pHead.next.next

        return dummy.next

# @lc code=end

