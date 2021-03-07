#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 重要，三种情况if - elif- else
        m, n = len(matrix), len(matrix[0])

        i, j = m - 1, 0
        while i >= 0 and j <= n-1:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        
        return False
# @lc code=end

