#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums = 0
        for num in nums:
            sums += num
        if sums%2 != 0:
            return False
        m, n = len(nums), sums/2

        #dp[i][j]: 对于前i个元素，使其和为j，共dp[i][j]种方法
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        
        if dp[i][j] > 0:
            return True
        else:
            return False
# @lc code=end

