#
# @lc app=leetcode.cn id=494 lang=python
#
# [494] 目标和
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = 0 
        for num in nums:
            sums += num
        if sums < S or (S + sums)%2 != 0: return 0 
        target = (S + sums) / 2
        m, n = len(nums), target
        # 定义dp[i][j], 对于前i个物品，从去取出若干使其总和为j时，总的方法数为dp[i][j]
        # 此时即有两种情况，即是否取第i个物品。条件是当前的容量是否够存第j个物品：
            # 如果不够存，则：
                # 则dp[i][j] = dp[i-1][j], 即与前i-1个物品情况完全相同；
            # 如果够存，则
                # 如果不取，dp[i][j] = dp[i-1][j]
                # 如果取，则dp[i][j] = dp[i-1][j-nums[i]]
            # 而对于当前情况而言，去或者不取都是一样的
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] 
        
        # 处理第一列的特殊情况，即对于前i个物品，总和为0，总的方法都是1中，不取
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(0, n+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        
        return dp[m][n]
# @lc code=end

