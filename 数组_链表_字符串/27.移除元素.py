#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left
# @lc code=end

