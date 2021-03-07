#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m, n = len(triangle), len(triangle[-1])
        if m == 1:
            return triangle[0][0]
        if m == 2:
            return min(triangle[-1]) + triangle[0][0] 

        dp = [[0 for i in range(n)] for i in range(m)]

        sums = 0
        # 处理第0列
        for i in range(m):
            sums += triangle[i][0]
            dp[i][0] = sums
        
        sums = 0
        # 处理对角线
        for i in range(m):
            sums += triangle[i][i]
            dp[i][i] = sums

        for i in range(2, m):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[-1])
# @lc code=end

