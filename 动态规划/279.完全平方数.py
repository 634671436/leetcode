#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

import math
# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 转化为凑零钱问题
        
        m = int(math.sqrt(n))
        nums = [(i+1)*(i+1) for i in range(m)]

        dp = [n+1 for _ in range(n+1)]
        dp[0] = 0

        for i in range(1, n+1):
            for j in nums:
                if i-j<0: continue
                dp[i] = min(dp[i], dp[i-j] + 1)
        
        return dp[n]
# @lc code=end

