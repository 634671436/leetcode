#
# @lc app=leetcode.cn id=714 lang=python
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # dp[i][k][0]: 第i天时不持有股票，且当前可以交易的最大次数为k次，此时最大利润为dp[i][k][0]；
        # dp[i][k][1]: 第i天时持有股票，且当前可以交易的最大次数为k次，此时最大利润为dp[i][k][1]；
        
        # dp[i][k][0] = max(dp[i-1][k][0],  dp[i-1][k][1]+price[i])
        #  不持有股票    i-1天也不持有(reset)      今天卖出(sell)
        # dp[i][k][1] = max(dp[i-1][k][1],  dp[i-1][k-1][0]-price[i]-fee)
        #   持有股票     i-1天也持有(reset)    i-1天不持有，今天买入(buy)

        # k=max简化为：
        # dp[i][max][0] = max(dp[i-1][max][0], dp[i-1][max][1]+price[i])
        # dp[i][max][1] = max(dp[i-1][max][1], dp[i-1][max-1][0]-price[i]-fee)
        #               = max(dp[i-1][max][1], dp[i-1][max][0]-price[i]-fee)
        # 简化为：
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0]-price[i]-fee)
        #          = max(dp[i-1][1], dp[i-1][0]-price[i]-fee)

        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                # 注意：第0天时持有则不仅需要支付估价，而且还得支付费用，所以-fee
                dp[i][1] = -prices[i] - fee  
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
            
        return dp[n-1][0]
        
# @lc code=end

