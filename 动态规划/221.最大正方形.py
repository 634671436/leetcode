#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        if m==0 or n==0:
            return 0

        # dp[i][j]定义：以matrix[i][j]为右下角，且只包含1的最大正方形的边长
        dp = [[0 for _ in range(n)] for _ in range(m)] 
        res = 0
        
        # 处理第一行
        for j in range(n):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                res = 1
        
        # 处理第一列
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                res = 1


        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    if dp[i][j] > res:
                        res = dp[i][j]
        
        return res * res

# @lc code=end

