#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[i] 表示凑出零钱i，需要的最少零钱个数
        # dp[i] 均赋值为amount+1，表示无法取到的最大值；
        # 此外，取min时由于有优先赋的较大值，因此直接利用min逐步比较计算最少数量
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin<0:continue
                dp[i] = min(dp[i], dp[i-coin]+1)  #设置较大值，再逐步比较计算min
        
        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]

# @lc code=end

