#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        chag_price = [0]
        for i in range(1, len(prices)):
            chag_price.append(prices[i]-prices[i-1])
        
        dp = [0 for i in range(len(prices))]

        for i in range(1, len(prices)):
            dp[i] = max(dp[i], dp[i-1] + chag_price[i])
        
        return max(dp)
        '''
        # dp[i][k][0]: 第i天时不持有股票，且当前可以交易的最大次数为k次，此时最大利润为dp[i][k][0]；
        # dp[i][k][1]: 第i天时持有股票，且当前可以交易的最大次数为k次，此时最大利润为dp[i][k][1]；
        
        # dp[i][k][0] = max(dp[i-1][k][0],  dp[i-1][k][1]+price[i])
        #  不持有股票    i-1天也不持有(reset)      今天卖出(sell)
        # dp[i][k][1] = max(dp[i-1][k][1],  dp[i-][k-1][0]-price[i])
        #   持有股票     i-1天也持有(reset)    i-1天不持有，今天买入(buy)

        # k=1简化为：
        # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+price[i])
        # dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-price[i])
        #             = max(dp[i-1][1][1], -price[i])
        # 即：
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i])
        # dp[i][1] = max(dp[i-1][1], -price[i])    # 只能买卖一次，如果今天买入，那之前就不能买入，之前利润为0

        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
        
        return dp[n-1][0]
# @lc code=end

