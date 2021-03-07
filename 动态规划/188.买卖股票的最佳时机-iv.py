#
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)]

        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    # 注意初始化条件
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
                        
        return dp[n-1][k][0]
# @lc code=end

