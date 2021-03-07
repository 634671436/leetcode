#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                return mid
            
            # mid 左侧有序
            if nums[mid] >= nums[left]:
                if nums[left] <= target and nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # mid 右侧有序
                if nums[mid] <= target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1 

        return -1
# @lc code=end

