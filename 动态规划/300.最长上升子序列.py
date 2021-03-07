#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        dp = [1 for i in range(m)]

        for i in range(1, m):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
# @lc code=end

