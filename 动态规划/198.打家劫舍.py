#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        max_money = max(dp[0], dp[1])

        for i in range(2, len(nums)):
            
            # 在dp[i-1]之前的所有位置遍历，加上当前位置的金钱，求这些位置的最大值
            tmp = [dp[j] + nums[i] for j in range(i-1)]
            dp[i] = max(tmp) 
            if dp[i] > max_money:
                max_money = dp[i]
        
        return max_money
# @lc code=end

