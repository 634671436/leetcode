#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # dp[i][k][0]:当前第i天且不持有股票，最多可以交易的次数为k次，利润为dp[i][k][0]
        # dp[i][k][1]:当前第i天，且持有归票，最多可以交易的次数为k次，利润为dp[i][k][1]

        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[s])

        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]

        for i in range(n):
            for k in range(2, 0, -1):
                if i == 0:
                    # 注意初始化条件
                    dp[i][1][0] = 0
                    dp[i][1][1] = -prices[i]
                    dp[i][2][0] = 0
                    dp[i][2][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                        
        return dp[n-1][2][0]
# @lc code=end

