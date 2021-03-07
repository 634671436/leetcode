#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        trace = ""
        self.dfs(n, 0, 0, trace)
        return self.res
    
    # left, right 维护当前string中左括号和右括号的数量
    def dfs(self, n, left, right, trace):
        
        # 返回条件：如果当前string中左括号比右括号少，即如 "()))", 则非法
        if left < right:
            return
        
        if left == n and right == n:
            self.res.append(trace)
        
        if left < n:
            self.dfs(n, left+1, right, trace + "(")
        
        if right < n:
            self.dfs(n, left, right+1, trace + ")" )


# @lc code=end

