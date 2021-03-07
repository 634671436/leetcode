#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = list(nums)
        max_num = nums[0]

        # dp[i]表示以nums[i]为结尾的连续序列的最大和        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            if dp[i] >= max_num:
                max_num = dp[i]
        
        return max_num

# @lc code=end

