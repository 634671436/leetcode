#
# @lc app=leetcode.cn id=287 lang=python
#
# [287] 寻找重复数
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                return nums[i]
# @lc code=end

