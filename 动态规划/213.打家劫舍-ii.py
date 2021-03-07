#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max( self.rob2(nums[0:len(nums)-1]), self.rob2(nums[1:len(nums)]) )

    def rob2(self, nums):
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
            
            # 在dp[i-1]之前的所有位置遍历，加上当前位置的金钱，求这些位置所有的最大值
            tmp = [dp[j] + nums[i] for j in range(i-1)]
            dp[i] = max(tmp) 
            if dp[i] > max_money:
                max_money = dp[i]
        
        return max_money
# @lc code=end

