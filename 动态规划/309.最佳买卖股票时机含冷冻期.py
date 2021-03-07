#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][k][0]: 第i天时不持有股票，且当前可以交易的最大次数为k次，此时最大利润为dp[i][k][0]；
        # dp[i][k][1]: 第i天时持有股票，且当前可以交易的最大次数为k次，此时最大利润为dp[i][k][1]；
        
        # dp[i][k][0] = max(dp[i-1][k][0],  dp[i-1][k][1]+price[i])
        #  不持有股票    i-1天也不持有(reset)      今天卖出(sell)
        # dp[i][k][1] = max(dp[i-1][k][1],  dp[i-1][k-2][0]-price[i])   冷冻期
        #   持有股票     i-1天也持有(reset)    i-1天不持有，今天买入(buy)

        # k=max简化为：
        # dp[i][max][0] = max(dp[i-1][max][0], dp[i-1][max][1]+price[i])
        # dp[i][max][1] = max(dp[i-1][max][1], dp[i-2][max-1][0]-price[i])
        #               = max(dp[i-1][max][1], dp[i-2][max][0]-price[i])
        
        # 简化为：
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0]-price[i])
        #          = max(dp[i-1][1], dp[i-2][0]-price[i])

        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            elif i == 1:
                # 注意这个地方的分析
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        
        return dp[n-1][0]

# @lc code=end

