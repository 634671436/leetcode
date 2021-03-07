#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] == target:
                return mid

        return left
# @lc code=end

