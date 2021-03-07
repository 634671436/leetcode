#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for i in range(n)] for i in range(m)]

        # 第0行
        path_flag = True
        for i in range(n):
            if path_flag and obstacleGrid[0][i] == 0:
                path_flag = True
                dp[0][i] = 1
            else:
                path_flag = False
                dp[0][i] = 0
        
        # 第0列
        path_flag = True
        for i in range(m):
            if path_flag and obstacleGrid[i][0] == 0:
                path_flag = True
                dp[i][0] = 1
            else:
                path_flag = False
                dp[i][0] = 0
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
                
        return dp[m-1][n-1]
                
# @lc code=end

