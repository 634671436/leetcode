#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        slow, fast = dummy, head

        # 与83题的区别在于，此时slow指针在相同的元素前一个位置，而在83题中，slow指针此时位于相同元素之上，所以无法下跳。
        # 而为了模拟fast自己前进，利用了fast.next.val的比较，自己向前移动
        while fast:
            if fast.next and fast.next.val != fast.val:
                slow = slow.next
            
            while fast.next and fast.next.val == fast.val:
                fast.next = fast.next.next
                # fast位于第一个重复的元素位置，如果有重复会一直移除元素，而slow.next = fast.next，slow此时已经与fast无必然联系了，只是fast中判断重复则在slow中去除
                # slow一直位于重复元素的前一个位置
                slow.next = fast.next
            
            fast = fast.next

        return dummy.next

# @lc code=end

