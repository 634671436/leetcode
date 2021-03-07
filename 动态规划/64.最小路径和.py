#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        dp = [[0 for i in range(n)] for i in range(m)]
        
        # 处理第0列
        sums = 0
        for i in range(m):
            sums += grid[i][0]
            dp[i][0] = sums

        # 处理第0行
        sums = 0
        for i in range(n):
            sums += grid[0][i]
            dp[0][i] = sums
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]

# @lc code=end

