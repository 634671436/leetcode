#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        self.direction = [(1,0), (-1,0), (0, 1), (0, -1)]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, grid)
        return count

    def dfs(self, i, j, grid):
        
        # 此题与79题单词搜索的差别在于所有的联通位置都被联系起来了，因为不存在回退的问题，也即不用masked再删除标记
        grid[i][j] = "#"
        for dx, dy in self.direction:
            nrow = i + dx
            ncols = j + dy
            # 这个地方注意是continue，也即对于当前位置[i][j]而言，如果一个方向[i+1][j]不行则换到下一个方向，而不是整个点都不打算走了
            if nrow < 0 or nrow >= len(grid) or ncols < 0 or ncols >= len(grid[0]) or grid[nrow][ncols] != "1" or self.dfs(nrow, ncols, grid):
                continue

# @lc code=end

