#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        # 重要！！
        masked = [[False for _ in range(n)] for _ in range(m)]

        self.direction = [(1,0), (0, -1), (-1, 0), (0, 1)]

        for i in range(m):
            for j in range(n):
                if self.search(i, j, board, 0, word, masked):
                    return True
        
        return False
    
    def search(self, i, j, board, index, word, masked):
        # 终止条件，找到word的最后一个位置，不相同
        if index == len(word) - 1:
            return board[i][j] == word[index]
        
        if board[i][j] == word[index]:
            # 将当前遍历的元素加入已经遍历的路径中，相当于把元素加入路径
            masked[i][j] = True

            for dx, dy in self.direction:
                # ！！注意，这里需要使用局部变量nrow, ncols
                nrow = i + dx
                ncols = j + dy
                
                # 注意判断条件 masked[nrow][ncols] == False，即不能跑重复的地方，比如往回跑
                if nrow >= 0 and nrow < len(board) and ncols >= 0 and ncols < len(board[0]) and masked[nrow][ncols] == False and self.search(nrow, ncols, board, index+1, word, masked):
                    return True
            
            # 把路径弹出来
            masked[i][j] = False

        return False 
    
        
# @lc code=end

