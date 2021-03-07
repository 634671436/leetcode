#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left, right = 0, n-1
        start, end = -1, -1
        while left <= right:
            mid = left + (right-left)/2
            # 寻找左边界
            if nums[mid] < target:
                left = mid + 1
            elif  nums[mid] >= target:
                right = mid - 1
        start = left
        
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left)/2
            # 寻找右边界
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] <= target:
                left = mid + 1
        end = right
        
        if start > end:
            return [-1, -1]
        
        return [start, end]
# @lc code=end

