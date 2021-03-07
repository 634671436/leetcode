#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        res = []
        for i in range(0, len(nums) - k + 1):
            res.append( max(nums[i:i+k]) )
        
        return res
# @lc code=end

