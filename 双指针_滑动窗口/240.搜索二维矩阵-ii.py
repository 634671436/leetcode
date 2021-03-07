#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1

        while i <= m-1 and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        
        return False
# @lc code=end

